# Part 2: Prompt Engineering and Evaluation

## Overview

**The uncomfortable truth:** Language models are like brilliant but unreliable employees. They can write beautiful code one moment and fabricate facts the next. They're creative when you need precision, and rigid when you need flexibility.

**Prompt engineering is how you manage this unpredictable genius.**

This isn't about "writing better prompts"—it's about **engineering reliable systems** from inherently unreliable components. Just as software engineers build fault-tolerant distributed systems, prompt engineers build consistent AI systems from stochastic language models.

**By the end of this section, you'll transform:**
- Random outputs → Consistent, predictable results
- Hallucinations → Fact-checked, grounded responses  
- Expensive verbosity → Cost-optimized precision
- Trial-and-error → Systematic, measurable improvement

---

## The Prompt Engineering Mindset

### Think Like a Systems Engineer, Not a Writer

**Common misconception:** "Prompt engineering is about being good with words"

**Reality:** Prompt engineering is about:
1. **Constraint design** - Defining boundaries for model behavior
2. **Template systems** - Building reusable, versioned components
3. **Quality metrics** - Measuring and optimizing performance
4. **Error handling** - Managing failures gracefully
5. **Cost optimization** - Balancing quality with efficiency

**Analogy:**

```
Writing Prompts : Prompt Engineering
        ↓                   ↓
Writing Code  :  Software Engineering
```

You're not just writing—you're building systems.

---

## Learning Objectives

By the end of this section, you'll be able to:

- ✅ **Craft** effective prompts: system roles, constraints, structured outputs, few-shot examples
- ✅ **Prevent** hallucinations with guardrails and validation techniques
- ✅ **Evaluate** prompts systematically for quality, stability, and cost-effectiveness
- ✅ **Optimize** parameters (temperature, top_p) for specific use cases
- ✅ **Implement** evaluation frameworks (LLM-as-judge, human-in-the-loop)
- ✅ **Build** production-ready prompt templates with version control and monitoring

---

## 2.0 Why Prompt Engineering Matters

### The Problem: Models Don't Read Your Mind

Language models are powerful, but they're not mind readers. Without proper guidance, they can produce outputs that are:
- **Inconsistent**: Same question, wildly different answers
- **Unreliable**: Hallucinated facts mixed with truth
- **Unusable**: Wrong format, wrong tone, or wrong scope
- **Inefficient**: Verbose responses when you need concise ones

Prompt engineering bridges the gap between what you want and what the model delivers.

### Real-World Impact: Before and After

#### Example 1: Customer Support Automation

**❌ Without Prompt Engineering:**
```python
# Simple, naive prompt
response = model.generate("Answer this customer question: How do I return a product?")
```

**Output:**
```
You can return products by following the return policy. Contact customer service 
for more information. Returns are usually processed within a few days.
```

**Problems:**
- Vague and unhelpful
- No specific steps
- Doesn't ask for order details
- Inconsistent tone across responses

**✅ With Prompt Engineering:**
```python
system_prompt = """
You are a customer support specialist for TechCorp with 5 years of experience.

Your role:
- Provide clear, step-by-step instructions
- Ask for necessary information (order number, purchase date)
- Reference specific policies with confidence
- Maintain a friendly, professional tone

Your constraints:
- Never promise refunds without verification
- Always collect order number before proceeding
- Escalate to human agent if issue is complex
- Keep responses under 100 words unless more detail is needed

Format:
1. Acknowledge the customer's concern
2. Ask for required information
3. Provide clear next steps
"""

response = model.generate(
    system_prompt=system_prompt,
    user_message="How do I return a product?",
    temperature=0.3  # Low temperature for consistency
)
```

**Output:**
```
I'd be happy to help you with your return! To get started, I'll need a few details:

1. Your order number (found in your confirmation email)
2. The date you received the product
3. The reason for the return

Once I have this information, I can guide you through our return process and 
provide you with a prepaid shipping label. Our return window is 30 days from 
the delivery date.
```

**Impact:**
- 40% reduction in follow-up questions
- 25% faster resolution time
- 90% customer satisfaction (up from 65%)

---

#### Example 2: Code Generation

**❌ Without Prompt Engineering:**
```python
response = model.generate("Write a function to validate email addresses")
```

**Output:**
```python
def validate_email(email):
    if "@" in email:
        return True
    return False
```

**Problems:**
- Oversimplified validation
- No error handling
- Missing edge cases
- No documentation

**✅ With Prompt Engineering:**
```python
prompt = """
Create a production-ready Python function to validate email addresses.

Requirements:
- Use regex for RFC 5322 compliance
- Handle edge cases (empty strings, None, special characters)
- Include comprehensive docstring with examples
- Add type hints
- Raise appropriate exceptions with clear messages
- Include unit test examples

Format:
1. Function with type hints
2. Docstring with description, args, returns, raises
3. Implementation with error handling
4. 3-5 test cases demonstrating usage
"""

response = model.generate(prompt, temperature=0.2)
```

**Output:**
```python
import re
from typing import Optional

def validate_email(email: Optional[str]) -> bool:
    """
    Validate an email address using RFC 5322 standards.
    
    Args:
        email: Email address string to validate
        
    Returns:
        bool: True if valid, False otherwise
        
    Raises:
        TypeError: If email is not a string or None
        
    Examples:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid.email")
        False
        >>> validate_email(None)
        False
    """
    if email is None:
        return False
    
    if not isinstance(email, str):
        raise TypeError(f"Expected string, got {type(email).__name__}")
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email.strip()))

# Test cases
assert validate_email("user@example.com") == True
assert validate_email("invalid") == False
assert validate_email("") == False
assert validate_email(None) == False
```

**Impact:**
- Production-ready code on first attempt
- 80% reduction in code review iterations
- Comprehensive documentation included

---

#### Example 3: Data Extraction

**❌ Without Prompt Engineering:**
```python
response = model.generate("Extract information from this text: John Smith bought 3 laptops on March 15, 2024 for $3,500")
```

**Output:**
```
The text mentions John Smith purchasing laptops in March 2024. He bought 3 laptops 
and spent $3,500.
```

**Problems:**
- Unstructured output
- Can't be parsed programmatically
- Missing fields
- Inconsistent format

**✅ With Prompt Engineering:**
```python
prompt = """
Extract structured information from the following text and return it as valid JSON.

Required fields:
- customer_name: Full name of the customer
- product: Product type
- quantity: Number of items (integer)
- purchase_date: Date in ISO 8601 format (YYYY-MM-DD)
- total_amount: Numeric value without currency symbol

If a field is not found, use null.

Text: {text}

Return ONLY valid JSON, no additional text.
"""

response = model.generate(
    prompt.format(text="John Smith bought 3 laptops on March 15, 2024 for $3,500"),
    temperature=0.0  # Deterministic for structured output
)
```

**Output:**
```json
{
  "customer_name": "John Smith",
  "product": "laptops",
  "quantity": 3,
  "purchase_date": "2024-03-15",
  "total_amount": 3500.00
}
```

**Impact:**
- 100% parseable output
- Enables automated downstream processing
- Consistent schema across all extractions

---

### Key Reasons Why Prompt Engineering Is Essential

#### 1. **Consistency Across Outputs**
Without prompt engineering, the same input can produce drastically different outputs. This is catastrophic for production systems.

**Example:** A legal document summarizer that sometimes includes opinions and sometimes doesn't is unusable.

#### 2. **Cost Optimization**
Better prompts = fewer tokens = lower costs.

**Example:** A well-crafted prompt can reduce output length by 50% while maintaining quality, cutting API costs in half.

#### 3. **Reliability and Trust**
Prompt engineering includes guardrails that prevent hallucinations and ensure factual accuracy.

**Example:** A medical information system must never fabricate drug interactions or dosages.

#### 4. **User Experience**
The right tone, format, and level of detail make or break user satisfaction.

**Example:** A technical documentation assistant that matches your company's style guide creates a seamless experience.

#### 5. **Scalability**
Prompt templates enable consistent behavior across thousands of requests without manual oversight.

**Example:** A content moderation system that reliably flags inappropriate content 24/7.

#### 6. **Measurability**
Well-engineered prompts produce structured outputs that can be evaluated and improved systematically.

**Example:** JSON outputs enable automated quality metrics and A/B testing.

---

### The Cost of Poor Prompting

**Real-world failure scenarios:**

1. **Chatbot Disaster**: A customer service bot without proper constraints promised free refunds to hundreds of customers, costing the company $50,000.

2. **Data Breach**: A document summarizer without proper guardrails leaked sensitive information by including it in summaries.

3. **Reputation Damage**: A content generator without tone constraints produced offensive responses, leading to public backlash.

4. **Wasted Resources**: A code generation tool without clear specifications required 5-10 iterations per request, making it slower than manual coding.

---

### What You'll Learn

In this chapter, you'll master:
- **System prompts** that define consistent behavior
- **Few-shot learning** to guide output format and style
- **Parameter tuning** for optimal creativity vs. consistency
- **Guardrails** to prevent hallucinations and errors
- **Evaluation frameworks** to measure and improve prompt quality
- **Production patterns** for scalable, maintainable prompt systems

By the end, you'll be able to transform unreliable model outputs into production-ready systems that deliver consistent, high-quality results.

---

## 2.1 Core Principles of Prompt Engineering

### System Prompts and Role Design

System prompts define the model's behavior, tone, and scope. They act as the foundation for consistent, reliable outputs.

By assigning a specific role (persona) to the model, you effectively narrow down the search space within the model's vast knowledge base. When a model adopts a persona, it aligns its vocabulary, tone, and reasoning style with that role. For example, a "senior engineer" persona will naturally prioritize efficiency, error handling, and scalability, whereas a "creative writer" persona will prioritize engagement and narrative flow. This technique, often called "persona adoption," is one of the most high-leverage changes you can make to a prompt.

#### Effective System Prompt Structure

```python
system_prompt = """
You are a [ROLE] with [EXPERTISE] specializing in [DOMAIN].

Your characteristics:
- [BEHAVIOR 1]
- [BEHAVIOR 2]
- [BEHAVIOR 3]

Your constraints:
- [CONSTRAINT 1]
- [CONSTRAINT 2]

Your output format:
- [FORMAT REQUIREMENT]
"""
```

#### Example: Technical Documentation Assistant

```python
system_prompt = """
You are a senior technical writer with 10 years of experience in software documentation.
You specialize in creating clear, concise, and accurate technical documentation for developers.

Your characteristics:
- Write in a professional but approachable tone
- Use active voice and present tense
- Include practical examples and code snippets
- Structure information logically with clear headings

Your constraints:
- Avoid jargon unless necessary (define when used)
- Keep sentences under 25 words when possible
- Provide step-by-step instructions for complex tasks
- Include troubleshooting sections for common issues

Your output format:
- Use Markdown formatting
- Include a brief overview section
- Structure content with hierarchical headings
- End with a summary or next steps section
"""
```

### Clear Instructions and Constraints

Ambiguity is the enemy of reliability. Models will default to the most probable continuation of your text, which is not always the most helpful one. To mitigate this, you must be explicit about what you want—and just as importantly, what you *don't* want.

Constraints act as guardrails. "Negative constraints" (telling the model what not to do) are often more powerful than positive instructions because they prune undesirable branches of the probability tree.

#### The CLEAR Framework

**C** - Context: Provide relevant background information
**L** - Length: Specify output length requirements
**E** - Examples: Show desired format and style
**A** - Audience: Define who will use the output
**R** - Requirements: List specific constraints and rules

#### Implementation Example

```python
def create_clear_prompt(task, context, length, examples, audience, requirements):
    return f"""
Context: {context}

Task: {task}

Requirements:
- Length: {length}
- Audience: {audience}
- {requirements}

Examples:
{examples}

Remember to follow all requirements and match the example format.
"""
```

### Few-Shot Learning and Reasoning

LLMs are excellent pattern matchers. "Few-shot learning" leverages this capability by providing examples of inputs and desired outputs within the prompt itself. This technique, also known as "in-context learning," allows the model to understand the task without weight updates (fine-tuning).

Instead of explaining a complex format in paragraphs of text, simply showing the model 3-5 examples often yields better results. It demonstrates tone, length, structure, and edge-case handling implicitly.

#### Few-Shot Pattern Design

```python
few_shot_prompt = """
Task: Generate product descriptions for e-commerce items.

Examples:

Input: Wireless Bluetooth Headphones
Output: Experience premium sound quality with our wireless Bluetooth headphones. 
Featuring active noise cancellation, 30-hour battery life, and comfortable 
over-ear design. Perfect for music lovers and professionals who demand 
exceptional audio performance.

Input: Stainless Steel Water Bottle
Output: Stay hydrated with our durable stainless steel water bottle. 
Double-wall vacuum insulation keeps drinks cold for 24 hours or hot for 12 hours. 
Leak-proof lid and sweat-free design make it perfect for gym, office, or outdoor adventures.

Input: Organic Cotton T-Shirt
Output:
"""
```

#### Reasoning Variants

For complex tasks requiring logic, math, or multi-step planning, standard prompting often fails because the model tries to guess the answer immediately. "Chain-of-Thought" (CoT) prompting forces the model to verbalize its thinking process before producing a final answer. This mimics human reasoning—breaking a hard problem into manageable steps—and significantly improves performance on reasoning tasks.

**Chain-of-Thought**: Step-by-step reasoning
```python
cot_prompt = """
Solve this problem step by step, showing your reasoning process.

Problem: A train travels 120 miles in 2 hours. What is its average speed?

Solution:
Step 1: Identify given information
- Distance = 120 miles
- Time = 2 hours

Step 2: Recall the formula
Speed = Distance ÷ Time

Step 3: Calculate
Speed = 120 miles ÷ 2 hours = 60 miles per hour

Answer: The train's average speed is 60 miles per hour.
"""
```

**Preamble Pattern**: Concise reasoning for production
```python
preamble_prompt = """
Before providing your answer, give a one-line explanation of your approach starting with "Preamble:"

Preamble: I'll calculate speed using the formula distance ÷ time.

The train's average speed is 60 miles per hour.
"""
```

## 2.2 Guardrails Against Hallinations

### Provenance Validation

Provenance validation is the process of grounding model outputs in verifiable source documents. It answers the question: "Where did this information come from?" By forcing the model to cite its sources or by verifying generated claims against a trusted knowledge base (RAG), you can drastically reduce hallucination rates. The goal is to ensure that every claim in the output can be traced back to a specific piece of evidence.

```python
class ProvenanceValidator:
    def __init__(self, source_documents):
        self.source_documents = source_documents
    
    def validate_claim(self, claim, source_text):
        """Check if a claim is supported by source text."""
        # Implement similarity checking
        # Use embeddings or keyword matching
        # Return confidence score and validation result
        
    def validate_response(self, response, sources):
        """Validate entire response against source documents."""
        claims = self.extract_claims(response)
        validation_results = []
        
        for claim in claims:
            supported = False
            for source in sources:
                if self.validate_claim(claim, source):
                    supported = True
                    break
            
            validation_results.append({
                'claim': claim,
                'supported': supported,
                'confidence': self.calculate_confidence(claim, sources)
            })
        
        return validation_results
```

### Trustworthiness Scoring

Not all model outputs are created equal. Trustworthiness scoring assigns a numerical confidence value to a response based on multiple heuristic signals. By evaluating factors such as internal consistency (does the model contradict itself?), factual accuracy (verified against tools), and logical coherence, you can filter out low-quality responses before they reach the user. This creates a reliability layer that sits between the raw model output and your application.

```python
class TrustworthinessScorer:
    def __init__(self, model_endpoint):
        self.model_endpoint = model_endpoint
    
    def score_response(self, response, context=None):
        """Calculate trustworthiness score for a response."""
        factors = {
            'consistency': self.check_consistency(response),
            'factual_accuracy': self.check_facts(response),
            'source_alignment': self.check_source_alignment(response, context),
            'logical_coherence': self.check_logic(response)
        }
        
        # Weighted scoring
        weights = {
            'consistency': 0.25,
            'factual_accuracy': 0.30,
            'source_alignment': 0.25,
            'logical_coherence': 0.20
        }
        
        score = sum(factors[key] * weights[key] for key in factors)\        \n        return {
            'score': score,
            'factors': factors,
            'recommendation': self.get_recommendation(score)
        }
    
    def get_recommendation(self, score):
        if score >= 0.8:
            return "High confidence - use as-is"
        elif score >= 0.6:
            return "Medium confidence - review recommended"
        else:
            return "Low confidence - verification required"
```

### Hallucination Detection Patterns

Hallucinations often leave linguistic fingerprints. While not foolproof, certain patterns in the model's output can signal a higher risk of fabrication. For instance, "excessive specificity" (making up very precise numbers or dates) or "hedging" (using vague authority like "experts say" without naming them) can indicate the model is filling in gaps. Detecting these patterns allows you to flag responses for human review or automatic regeneration.

```python
def detect_potential_hallucinations(response):
    """Identify potential hallucination indicators."""
    indicators = {
        'excessive_specificity': len(re.findall(r'\d+', response)) > 10,
        'unverifiable_claims': any(phrase in response.lower() for phrase in [
            'studies show', 'research indicates', 'experts say'
        ]),
        'temporal_inconsistencies': check_temporal_consistency(response),
        'factual_contradictions': check_factual_consistency(response)
    }
    
    risk_score = sum(indicators.values()) / len(indicators)
    return {
        'risk_score': risk_score,
        'indicators': indicators,
        'needs_review': risk_score > 0.5
    }
```

## 2.3 Parameter Tuning for Stability and Style

### Temperature and Top_p Fundamentals

These two parameters control the randomness of the model's output distribution, but they do so in different ways.

**Temperature (0.0 - 2.0)**:
Temperature scales the logits (raw prediction scores) before they are converted to probabilities.
- **Low Temperature (< 0.5)**: Sharpens the probability distribution. The model becomes highly conservative, sticking to the most likely tokens. Great for coding, data extraction, and factual Q&A.
- **High Temperature (> 0.8)**: Flattens the distribution. The model takes more risks, choosing less probable tokens. This fuels creativity but increases the chance of errors and hallucinations.

**Top_p (Nucleus Sampling) (0.0 - 1.0)**:
Top_p cuts off the long tail of unlikely tokens. Instead of considering the entire vocabulary, the model only considers the smallest set of top tokens whose cumulative probability exceeds `p`.
- **Low Top_p (< 0.5)**: Forces the model to choose from only the very best options.
- **High Top_p (> 0.9)**: Allows for a wider vocabulary and more diverse phrasing.

*Best Practice:* Generally, tune one or the other, not both simultaneously. A common pattern is to fix Top_p (e.g., at 0.9) and vary Temperature to control creativity.

### Practical Parameter Ranges

Different tasks require different "cognitive settings." Just as you wouldn't ask a poet to do your taxes, you shouldn't use creative settings for data extraction. Defining "profiles" for your prompts helps standardize these settings across your team and application.

```python
PARAMETER_PROFILES = {
    'accuracy_focused': {
        'temperature': 0.1,
        'top_p': 0.3,
        'description': 'High accuracy, low creativity'
    },
    'balanced': {
        'temperature': 0.5,
        'top_p': 0.7,
        'description': 'Balanced creativity and accuracy'
    },
    'creative': {
        'temperature': 0.8,
        'top_p': 0.9,
        'description': 'High creativity, varied outputs'
    },
    'deterministic': {
        'temperature': 0.0,
        'top_p': 0.1,
        'description': 'Maximum consistency'
    }
}
```

### Parameter Sensitivity Testing

Finding the perfect parameters is often an empirical process. Small changes in temperature can lead to vastly different user experiences. Parameter sensitivity testing involves systematically running the same prompt across a grid of settings to observe how the output behavior changes. This helps you find the "sweet spot" where the model is creative enough to be engaging but stable enough to be reliable.

```python
class ParameterSensitivityTester:
    def __init__(self, client, test_prompts):
n        self.client = client
        self.test_prompts = test_prompts
    
    def test_parameter_combinations(self, param_grid):
        """Test multiple parameter combinations."""
        results = []
        
        for temp, top_p in param_grid:
            combination_results = {
                'temperature': temp,
                'top_p': top_p,
                'outputs': [],
                'metrics': {}
            }
            
            for prompt in self.test_prompts:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=temp,
                    top_p=top_p
                )
                
                combination_results['outputs'].append({
                    'prompt': prompt,
                    'response': response.choices[0].message.content
                })
            
            # Calculate metrics for this combination
            combination_results['metrics'] = self.calculate_metrics(
                combination_results['outputs']
            )
            
            results.append(combination_results)
        
        return results
    
    def calculate_metrics(self, outputs):
        """Calculate stability and quality metrics."""
        responses = [output['response'] for output in outputs]
        
        return {
            'avg_length': np.mean([len(r) for r in responses]),
            'length_variance': np.var([len(r) for r in responses]),
            'lexical_diversity': self.calculate_lexical_diversity(responses),
            'consistency_score': self.calculate_consistency(responses)
        }
```

## 2.4 Evaluation Frameworks

### LLM-as-a-Judge Implementation

Evaluating generative AI is hard because there is no single "correct" answer. Traditional metrics like BLEU or ROUGE (used in translation) correlate poorly with human judgment for open-ended tasks.

"LLM-as-a-Judge" is a powerful pattern where you use a highly capable model (like GPT-4) to evaluate the outputs of a smaller or faster model (like GPT-3.5 or a local model). By providing the judge with a rubric and specific criteria, you can automate the evaluation process, getting consistent, explained scores that correlate well with human preference.

```python
class LLMJudge:
    def __init__(self, judge_model_client):
        self.judge_model = judge_model_client
    
    def evaluate_response(self, response, criteria, reference=None):
        """Evaluate a response using LLM-as-judge."""
        evaluation_prompt = f"""
You are an expert evaluator. Assess the following response based on these criteria:

Criteria: {criteria}

{f"Reference answer: {reference}" if reference else ""}

Response to evaluate: {response}

Provide scores (1-10) for each criterion and brief justifications:
- Relevance: [score] - [justification]
- Accuracy: [score] - [justification] 
- Clarity: [score] - [justification]
- Completeness: [score] - [justification]
- Style: [score] - [justification]

Overall score: [average]/10
"""
        
        evaluation = self.judge_model.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": evaluation_prompt}]
        )
        
        return self.parse_evaluation(evaluation.choices[0].message.content)
    
    def batch_evaluate(self, responses, criteria):
        """Evaluate multiple responses efficiently."""
        evaluations = []
        
        for response in responses:
            evaluation = self.evaluate_response(response, criteria)
            evaluations.append(evaluation)
        
        return self.aggregate_evaluations(evaluations)
```

### Human-in-the-Loop Evaluation

While automated metrics are fast, human judgment remains the gold standard. Human-in-the-loop (HITL) evaluation is essential for:
1.  **Validating the Judge:** Checking if your LLM-as-a-judge is actually accurate.
2.  **Edge Cases:** Catching subtle errors or safety issues that automated systems miss.
3.  **Ground Truth:** Creating a high-quality dataset for future fine-tuning.

A good HITL framework presents reviewers with a clear interface, specific questions, and comparison tasks (A/B testing) rather than vague "is this good?" prompts.

```python
class HumanEvaluationFramework:
    def __init__(self, evaluation_interface):
        self.interface = evaluation_interface
    
    def create_evaluation_task(self, responses, criteria):
        """Create structured evaluation tasks for human reviewers."""
        tasks = []
        
        for i, response in enumerate(responses):
            task = {
                'task_id': f'eval_{i}',
                'response': response,
                'criteria': criteria,
                'questions': self.generate_evaluation_questions(criteria)
            }
            tasks.append(task)
        
        return tasks
    
    def generate_evaluation_questions(self, criteria):
        """Generate specific questions for each criterion."""
        questions = {}
        
        for criterion in criteria:
            if criterion == 'relevance':
                questions[criterion] = "How relevant is this response to the prompt? (1-5)"
            elif criterion == 'accuracy':
                questions[criterion] = "How accurate is the information provided? (1-5)"
            elif criterion == 'clarity':
                questions[criterion] = "How clear and understandable is the response? (1-5)"
        
        return questions
    
    def collect_feedback(self, task_results):
        """Collect and analyze human feedback."""
        aggregated_results = {
            'average_scores': {},
            'agreement_scores': {},
            'qualitative_feedback': []
        }
        
        for criterion in task_results[0]['scores']:
            scores = [result['scores'][criterion] for result in task_results]
            aggregated_results['average_scores'][criterion] = np.mean(scores)
            aggregated_results['agreement_scores'][criterion] = self.calculate_agreement(scores)
        
        return aggregated_results
```

## 2.5 Production-Ready Prompt Templates

### Template Management System

Hardcoding prompts directly into your application code is a recipe for technical debt. It makes them hard to update, version, or test without redeploying the entire application.

A "Prompt Template Management System" treats prompts as first-class assets. It separates the prompt logic (the text template) from the application logic (the code). This allows non-technical team members (like prompt engineers or domain experts) to iterate on prompts independently, and it enables features like localization, versioning, and dynamic substitution.

```python
class PromptTemplateManager:
    def __init__(self, template_dir):
        self.template_dir = template_dir
        self.templates = {}
        self.load_templates()
    
    def load_templates(self):
        """Load templates from directory."""
        for filename in os.listdir(self.template_dir):
            if filename.endswith('.json'):
                with open(os.path.join(self.template_dir, filename)) as f:
                    template = json.load(f)
                    self.templates[template['name']] = template
    
    def get_template(self, name, **kwargs):
        """Get template with variable substitution."""
        if name not in self.templates:
            raise ValueError(f"Template '{name}' not found")
        
        template = self.templates[name]
        prompt = template['template']
        
        # Substitute variables
        for key, value in kwargs.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        
        return prompt
    
    def validate_template(self, template):
        """Validate template structure and content."""
        required_fields = ['name', 'version', 'template', 'parameters']
        
        for field in required_fields:
            if field not in template:
                raise ValueError(f"Missing required field: {field}")
        
        # Validate parameters
        for param in template['parameters']:
            if 'name' not in param or 'type' not in param:
                raise ValueError("Parameter must have 'name' and 'type'")
        
        return True
```

### Version Control and A/B Testing

Prompts are code. They should be versioned, reviewed, and tested just like any other software component. When you change a prompt, you need to know:
1.  **What changed?** (Diffs)
2.  **Why did it change?** (Commit messages/Metadata)
3.  **Did it get better?** (A/B Testing)

A/B testing allows you to scientifically measure the impact of a prompt change on real-world metrics (like user acceptance rate or conversion). By serving different versions to a subset of users, you can make data-driven decisions about which prompt performs best.

```python
from typing import Dict, Optional, List, Any
from datetime import datetime
import uuid

class PromptVersionControl:
    """Manages versioning and deployment of prompt templates."""
    
    def __init__(self, storage_backend: Any):
        self.storage = storage_backend
    
    def generate_version_id(self) -> str:
        """Generate a unique version identifier."""
        return str(uuid.uuid4())

    def create_version(
        self, 
        template_name: str, 
        template_content: str, 
        metadata: Optional[Dict[str, Any]] = None
    ) -> str:
        """Create and save a new version of a prompt template."""
        version_id = self.generate_version_id()
        
        version_data = {
            'template_name': template_name,
            'version_id': version_id,
            'content': template_content,
            'created_at': datetime.now().isoformat(),
            'metadata': metadata or {}
        }
        
        self.storage.save_version(version_data)
        return version_id
    
    def deploy_version(
        self, 
        template_name: str, 
        version_id: str, 
        traffic_percentage: int = 100
    ) -> Dict[str, Any]:
        """
        Deploy a specific version to production.
        
        Args:
            template_name: Name of the template
            version_id: ID of the version to deploy
            traffic_percentage: 0-100 percentage of traffic to route to this version
        """
        deployment = {
            'template_name': template_name,
            'version_id': version_id,
            'traffic_percentage': traffic_percentage,
            'deployed_at': datetime.now().isoformat()
        }
        
        self.storage.save_deployment(deployment)
        return deployment
    
    def run_ab_test(
        self, 
        template_name: str, 
        version_a: str, 
        version_b: str, 
        traffic_split: int = 50
    ) -> Dict[str, Any]:
        """
        Configure an A/B test between two prompt versions.
        
        Returns:
            Configuration dictionary for the experiment
        """
        test_config = {
            'template_name': template_name,
            'version_a': version_a,
            'version_b': version_b,
            'traffic_split': traffic_split,
            'start_time': datetime.now().isoformat(),
            'metrics': ['conversion_rate', 'user_satisfaction', 'response_quality']
        }
        
        return test_config
```

## 2.6 Implementation Examples

### Example 1: Customer Support Bot

This example demonstrates how to combine **System Prompts**, **Few-Shot Learning**, and **Context Injection** to create a robust customer service agent. Notice how the system prompt sets firm boundaries (e.g., "Never make promises about refunds"), while the few-shot examples guide the tone and format of the interaction.

```python
class CustomerSupportBot:
    def __init__(self, model_client):
        self.model = model_client
        self.setup_prompts()
    
    def setup_prompts(self):
        self.system_prompt = """
You are a helpful customer support assistant for TechCorp.
You have access to order information, product details, and troubleshooting guides.

Guidelines:
- Be polite and professional
- Ask clarifying questions when needed
- Provide step-by-step solutions
- Escalate to human agent for complex issues
- Never make promises about refunds or compensation
"""
        
        self.few_shot_examples = [
            {
                "user": "My order hasn't arrived yet.",
                "assistant": "I'd be happy to help you track your order. Could you please provide your order number so I can check the status for you?"
            },
            {
                "user": "The product is broken.",
                "assistant": "I'm sorry to hear that. Can you describe what's wrong with the product? Also, when did you receive it? This will help me determine the best way to assist you."
            }
        ]
    
    def generate_response(self, user_message, order_context=None):
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Add few-shot examples
        for example in self.few_shot_examples:
            messages.extend([
                {"role": "user", "content": example["user"]},
                {"role": "assistant", "content": example["assistant"]}
            ])
        
        # Add context if available
        if order_context:
            messages.append({
                "role": "system",
                "content": f"Context: {order_context}"
            })
        
        messages.append({"role": "user", "content": user_message})
        
        response = self.model.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.3,  # Low temperature for consistency
            max_tokens=150
        )
        
        return response.choices[0].message.content
```

### Example 2: Content Quality Evaluator

This example showcases the **LLM-as-a-Judge** pattern. Instead of generating content for a user, the model is acting as a critic. The prompt is structured with a clear persona ("expert content evaluator") and a detailed rubric (clarity, accuracy, etc.). This allows for structured, quantitative feedback on qualitative text.

```python
class ContentQualityEvaluator:
    def __init__(self, judge_model):
        self.judge = judge_model
        self.evaluation_criteria = {
            'clarity': 'Is the content clear and easy to understand?',
            'accuracy': 'Is the information factually correct?',
            'completeness': 'Does it cover all necessary aspects?',
            'engagement': 'Is the content engaging and interesting?',
            'seo_optimization': 'Is the content optimized for search engines?'
        }
    
    def evaluate_content(self, content, target_audience, purpose):
        evaluation_prompt = f"""
You are an expert content evaluator. Assess the following content based on these criteria:

Target Audience: {target_audience}
