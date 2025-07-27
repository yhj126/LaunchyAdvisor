LaunchyAdvisor is an intelligent assistant designed to simulate a team of business domain experts helping startups evaluate strategic questions — such as launching a new product in a specific region.

This project was developed as part of the **Launchyfi Intern Build Challenge** and showcases agent orchestration, modular design, and local/offline LLM integration with **Ollama**.

This application uses a modular architecture where each expert agent provides insights in a specific area (Budget, Legal, and Marketing), coordinated by an Orchestrator Agent.
---

## 🧠 How it works

The system is composed of:

- **`BudgetExpert`**: Assesses financial feasibility.
- **`LegalExpert`**: Reviews legal considerations (e.g., GDPR).
- **`MarketingExpert`**: Evaluates market strategy and regional fit.
- **`OrchestratorAgent`**: Coordinates agents and synthesizes a final structured response.

You can switch between two modes:
- ✅ **Local simulation (hardcoded logic)**
- 🤖 **LLM via Ollama (optional)**

---

## 📦 Requirements

- Python 3.8+
- (Optional) [Ollama](https://ollama.com) installed locally for LLM support
- Deepseek-r1 model(https://ollama.com/library/deepseek-r1)

Install dependencies (only needed if using Ollama):
```bash
pip install -r requirements.txt
```

## 🚀 Running the App

Run the app from the terminal:
```bash
python main.py
```
You will be prompted to enter a business question, for example:
```bash
❓ Enter your business question:
> Can we launch an AI product in Germany next quarter?
```

## 🤖 Using Ollama (Optional)

To use a local LLM instead of hardcoded logic:

    Install Ollama: https://ollama.com

    Start the model you want, e.g.:
    
```bash
ollama run llama3
```
Haojie Yin
Computer Engineering Graduate
