# Week 6 sample data

## `sample_job_postings.csv` (real data)

A small classroom subset (~60 rows) of **real** job postings, filtered to
tech/data roles so the "skill analyzer / learning path" theme is relevant.

- **Source dataset:** `xanderios/linkedin-job-postings` on the Hugging Face
  Hub — a no-login mirror of the Kaggle
  [LinkedIn Job Postings (2023-2024)](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings)
  dataset cited in the Week 6 README.
- **How it was built:** `scripts/build_job_postings_sample.py` reads rows
  through the public Hugging Face datasets-server JSON API (no auth, standard
  library only), keeps tech/data titles, maps the columns onto the Week 6
  schema, and truncates each `job_description` to ~1500 characters to keep the
  file small. Re-run the script to regenerate the file deterministically.
- **Step-by-step version:** `scripts/build_job_postings_sample.ipynb` is the
  same process explained and demonstrated cell by cell (inspect the raw API
  response, the schema mapping, the tech/data filter, then collect and verify).
  It writes the identical CSV.

### Columns

```text
job_id, job_title, company, location, job_description, job_skills, posted_date, source
```

### Known limitations of this subset

- `company` is empty: the HF mirror only carries a numeric `company_id`, not a
  company name (the original Kaggle release ships company names in a separate
  `companies.csv`).
- `job_skills` is sparse: the upstream `skills_desc` field is usually empty, so
  the analyzer is expected to infer skills from `job_description` text.
- Descriptions are truncated to ~1500 characters. For a stronger final project,
  download a larger prepared subset yourself and follow the dataset's license
  and terms.

## `sample_job_postings_classroom.csv` (handcrafted backup)

The original handcrafted classroom sample (8 rows). Kept as a tiny,
fully-populated example (including `company` and `job_skills`) that is handy for
quick demos and unit-test-style checks.

## Other samples

`sample_customer_feedback.csv`, `sample_product_reviews.csv`, and
`sample_sales.csv` support the optional alternate themes described in the Week 6
README. Keep the same input/output contract if you adapt the pipeline to them.
