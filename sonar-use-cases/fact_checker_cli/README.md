# Fact Checker CLI

A command-line tool that identifies false or misleading claims in articles or statements using Perplexity's Sonar API for web research.

## Features

- Analyze claims or entire articles for factual accuracy  
- Identify false, misleading, or unverifiable claims  
- Provide explanations and corrections for inaccurate information  
- Output results in human-readable format or structured JSON  
- Cite reliable sources for fact-checking assessments  
- Leverages Perplexity's structured outputs for reliable JSON parsing (for Tier 3+ users)

## Installation

### 1. Install required dependencies

```bash
# Ensure you are using the same pip associated with the python3 you intend to run the script with
pip install requests pydantic newspaper3k lxml-html-clean
```

### 2. Make the script executable

```bash
chmod +x fact_checker.py
```

## API Key Setup

The tool requires a Perplexity API key to function. You can provide it in one of these ways:

### 1. As a command-line argument

```bash
./fact_checker.py --api-key YOUR_API_KEY
```

### 2. As an environment variable

```bash
export PPLX_API_KEY=YOUR_API_KEY
```

### 3. In a file

Create a file named `pplx_api_key` or `.pplx_api_key` in the same directory as the script:

```bash
echo "YOUR_API_KEY" > .pplx_api_key
chmod 600 .pplx_api_key
```

**Note:** If you're using the structured outputs feature, you'll need a Perplexity API account with Tier 3 or higher access level.

## Quick Start

Run the following command immediately after setup:

```bash
./fact_checker.py -t "The Earth is flat and NASA is hiding the truth."
```

This will analyze the claim, research it using Perplexity's Sonar API, and return a detailed fact check with ratings, explanations, and sources.

## Usage

### Check a claim

```bash
./fact_checker.py --text "The Earth is flat and NASA is hiding the truth."
```

### Check an article from a file

```bash
./fact_checker.py --file article.txt
```

### Check an article from a URL

```bash
./fact_checker.py --url https://www.example.com/news/article-to-check
```

### Specify a different model

```bash
./fact_checker.py --text "Global temperatures have decreased over the past century." --model "sonar-pro"
```

### Output results as JSON

```bash
./fact_checker.py --text "Mars has a breathable atmosphere." --json
```

### Use a custom prompt file

```bash
./fact_checker.py --text "The first human heart transplant was performed in the United States." --prompt-file custom_prompt.md
```

### Enable structured outputs (for Tier 3+ users)

Structured output is disabled by default. To enable it, pass the `--structured-output` flag:

```bash
./fact_checker.py --text "Vaccines cause autism." --structured-output
```

### Get help

```bash
./fact_checker.py --help
```

## Output Format

The tool provides output including:

- **Overall Rating**: MOSTLY_TRUE, MIXED, or MOSTLY_FALSE
- **Summary**: A brief overview of the fact-checking findings
- **Claims Analysis**: A list of specific claims with individual ratings:
  - TRUE: Factually accurate and supported by evidence
  - FALSE: Contradicted by evidence
  - MISLEADING: Contains some truth but could lead to incorrect conclusions
  - UNVERIFIABLE: Cannot be conclusively verified with available information
- **Explanations**: Detailed reasoning for each claim
- **Sources**: Citations and URLs used for verification

## Example

Run the following command:

```bash
./fact_checker.py -t "The Great Wall of China is visible from the moon."
```

Example output:

```
Fact checking in progress...

🔴 OVERALL RATING: MOSTLY_FALSE

📝 SUMMARY:
The claim that the Great Wall of China is visible from the moon is false. This is a common misconception that has been debunked by NASA astronauts and scientific evidence.

🔍 CLAIMS ANALYSIS:

Claim 1: ❌ FALSE  
  Statement: "The Great Wall of China is visible from the moon."  
  Explanation: The Great Wall of China is not visible from the moon with the naked eye. NASA astronauts have confirmed this, including Neil Armstrong who stated he could not see the Wall from lunar orbit. The Wall is too narrow and is similar in color to its surroundings when viewed from such a distance.  
  Sources:
    - NASA.gov
    - Scientific American
    - National Geographic
```

## Limitations

- The accuracy of fact-checking depends on the quality of information available through the Perplexity Sonar API.
- Like all language models, the underlying AI may have limitations in certain specialized domains.
- The structured outputs feature requires a Tier 3 or higher Perplexity API account.
- The tool does not replace professional fact-checking services for highly sensitive or complex content.
