# 📝 AI Blog Generation Agent

An AI-powered blog generation application built using **LangGraph** and **LLMs** to automatically create blog content from a given topic.

The application uses an agentic workflow where different stages of the blog creation process are orchestrated as a graph. The generated content can be tested and interacted with through **LangGraph Studio**.

---

## 🚀 What Does This Project Do?

Simply provide a topic, and the AI agent generates a blog around it.

For example:

> **Input:** "Impact of Artificial Intelligence on Healthcare"

The agent can generate:

- A suitable blog title
- Structured blog content
- Well-organized sections
- Content tailored to the requested topic

The application is designed as an **agentic workflow**, making it easier to extend the solution with additional AI capabilities in the future.

---

## 🏗️ Architecture

The application uses **LangGraph** to orchestrate the blog generation workflow.

```text
                User
                  │
                  ▼
             Enter Topic
                  │
                  ▼
        ┌──────────────────┐
        │   Title Creation │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Content Generation│
        └────────┬─────────┘
                 │
                 ▼
          Generated Blog
                 │
                 ▼
               User