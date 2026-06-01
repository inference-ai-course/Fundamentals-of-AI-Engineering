#!/usr/bin/env python3
"""
Template for structured information extraction using LLM.

This script demonstrates:
1. Defining a JSON schema for structured output
2. Calling an LLM with the schema as a constraint
3. Validating the output against the schema
4. Retrying/repairing invalid outputs

Usage:
    python extract_template.py --input "John Smith, email: john@example.com, phone: 555-1234"
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

try:
    import requests
except ImportError:
    print("Error: requests is required. Install with: pip install requests")
    sys.exit(1)


# ============================================================================
# JSON Schema Definition
# ============================================================================

# Example: Contact information extraction schema
CONTACT_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "Full name of the person"
        },
        "email": {
            "type": "string",
            "format": "email",
            "description": "Email address"
        },
        "phone": {
            "type": "string",
            "description": "Phone number in any format"
        },
        "company": {
            "type": "string",
            "description": "Company or organization name"
        }
    },
    "required": ["name", "email"]
}

# Example: Product information extraction schema
PRODUCT_SCHEMA = {
    "type": "object",
    "properties": {
        "product_name": {
            "type": "string",
            "description": "Name of the product"
        },
        "price": {
            "type": "number",
            "description": "Price in USD"
        },
        "category": {
            "type": "string",
            "enum": ["electronics", "clothing", "books", "home", "sports", "other"],
            "description": "Product category"
        },
        "in_stock": {
            "type": "boolean",
            "description": "Whether the product is in stock"
        }
    },
    "required": ["product_name", "price"]
}


# ============================================================================
# Extraction Functions
# ============================================================================

def build_extraction_prompt(text: str, schema: Dict[str, Any]) -> str:
    """Build a prompt for structured extraction."""
    return f"""Extract structured information from the following text.

Output ONLY valid JSON that matches this schema:
{json.dumps(schema, indent=2)}

Text to extract from:
{text}

JSON output:"""


def call_ollama(
    prompt: str,
    model: str = "llama3.1",
    host: str = "http://localhost:11434",
    timeout_s: float = 60.0
) -> str:
    """Call Ollama API."""
    url = f"{host}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "format": "json"  # Request JSON output
    }
    
    resp = requests.post(url, json=payload, timeout=timeout_s)
    resp.raise_for_status()
    data = resp.json()
    return data.get("response", "")


def validate_json_output(text: str, schema: Dict[str, Any]) -> Dict[str, Any]:
    """Validate JSON output against schema."""
    # Try to parse JSON
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        return {"valid": False, "error": f"JSON parse error: {e}", "data": None}
    
    # Check required fields
    missing = []
    for field in schema.get("required", []):
        if field not in data:
            missing.append(field)
    
    if missing:
        return {
            "valid": False,
            "error": f"Missing required fields: {missing}",
            "data": data
        }
    
    # Check field types (basic validation)
    properties = schema.get("properties", {})
    type_errors = []
    
    for field, value in data.items():
        if field in properties:
            expected_type = properties[field].get("type")
            if expected_type == "string" and not isinstance(value, str):
                type_errors.append(f"{field} should be string")
            elif expected_type == "number" and not isinstance(value, (int, float)):
                type_errors.append(f"{field} should be number")
            elif expected_type == "boolean" and not isinstance(value, bool):
                type_errors.append(f"{field} should be boolean")
    
    if type_errors:
        return {
            "valid": False,
            "error": f"Type errors: {type_errors}",
            "data": data
        }
    
    return {"valid": True, "error": None, "data": data}


def extract_with_retry(
    text: str,
    schema: Dict[str, Any],
    model: str = "llama3.1",
    max_retries: int = 3
) -> Dict[str, Any]:
    """Extract structured data with retry logic."""
    prompt = build_extraction_prompt(text, schema)
    
    for attempt in range(max_retries):
        print(f"Attempt {attempt + 1}/{max_retries}...")
        
        try:
            raw_output = call_ollama(prompt, model=model)
            print(f"  Raw output: {raw_output[:100]}...")
            
            result = validate_json_output(raw_output, schema)
            
            if result["valid"]:
                print("  ✓ Valid JSON output")
                return result["data"]
            else:
                print(f"  ✗ Validation failed: {result['error']}")
                
                # Try to repair the output
                if result["data"]:
                    repaired = repair_output(result["data"], schema)
                    if repaired:
                        print("  ✓ Repaired output")
                        return repaired
                
                # Add error context to prompt for retry
                prompt = build_repair_prompt(text, schema, raw_output, result["error"])
        
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    print("All retries exhausted")
    return {}


def repair_output(data: Dict[str, Any], schema: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Attempt to repair invalid output."""
    # Fill missing required fields with defaults
    repaired = data.copy()
    
    for field in schema.get("required", []):
        if field not in repaired:
            properties = schema.get("properties", {})
            if field in properties:
                field_type = properties[field].get("type")
                if field_type == "string":
                    repaired[field] = ""
                elif field_type == "number":
                    repaired[field] = 0
                elif field_type == "boolean":
                    repaired[field] = False
    
    # Validate again
    result = validate_json_output(json.dumps(repaired), schema)
    return repaired if result["valid"] else None


def build_repair_prompt(
    text: str,
    schema: Dict[str, Any],
    invalid_output: str,
    error: str
) -> str:
    """Build a prompt to repair invalid output."""
    return f"""The previous output was invalid. Please fix it.

Error: {error}

Original text:
{text}

Required schema:
{json.dumps(schema, indent=2)}

Previous (invalid) output:
{invalid_output}

Output ONLY valid JSON that matches the schema:"""


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Extract structured information from text using LLM"
    )
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Input text to extract from"
    )
    parser.add_argument(
        "--schema",
        choices=["contact", "product"],
        default="contact",
        help="Schema to use for extraction"
    )
    parser.add_argument(
        "--model",
        default="llama3.1",
        help="LLM model to use"
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=3,
        help="Maximum retry attempts"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output JSON file path"
    )
    
    args = parser.parse_args()
    
    # Select schema
    schema = CONTACT_SCHEMA if args.schema == "contact" else PRODUCT_SCHEMA
    print(f"Using schema: {args.schema}")
    
    # Extract
    result = extract_with_retry(
        args.input,
        schema,
        model=args.model,
        max_retries=args.max_retries
    )
    
    # Output
    output_json = json.dumps(result, indent=2)
    print(f"\nExtracted data:\n{output_json}")
    
    if args.output:
        with open(args.output, "w") as f:
            f.write(output_json)
        print(f"\nSaved to: {args.output}")


if __name__ == "__main__":
    main()