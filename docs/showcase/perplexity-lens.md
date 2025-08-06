---
title: Perplexity Lens
description: A browser extension that builds personalized knowledge graphs using Perplexity AI
sidebar_position: 1
keywords: [browser extension, knowledge graph, RAG, summarization]
---




# Perplexity Lens 🔍

**Perplexity Lens** is a powerful browser extension that transforms your browsing experience. It provides AI-powered insights using Perplexity AI and creates a **personalized knowledge graph** that visually connects the concepts you encounter online.

## Features

- 🔍 **Smart Text Selection**: Get AI-generated explanations for selected text.
- 📄 **Webpage Summarization**: Instantly summarize an entire webpage for quick understanding.
- 🧠 **Contextual RAG Insights**: Retrieve detailed context or concise meanings for any word or phrase using Retrieval-Augmented Generation (RAG).
- 📊 **Knowledge Graph Visualization**: Explore connections between ideas using an interactive graph built with D3.js.
- 🔗 **Public Sharing**: Generate URLs for sharing your graph with others.
- 🔐 **User Authentication**: Secure access with Firebase.
- 💾 **Dual Storage**: Store data locally via IndexedDB and in the cloud via Firebase.
- 📱 **Responsive UI**: Fully functional across devices.
- 🎨 **Modern Stack**: Built using React, TypeScript, and TailwindCSS.

## Prerequisites

Before using Perplexity Lens, ensure you have:

- Node.js (v14 or later)
- npm (v6 or later)
- Google Chrome (or compatible browser)
- Firebase account for cloud functionality
- Firebase CLI (`npm install -g firebase-tools`)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/perplexity-lens.git
   cd perplexity_lens
   ```

2. **Install Dependencies:**
   ```bash
   npm install
   ```

3. **Configure API Keys:**
   Edit `src/config.ts`:
   ```ts
   export const PERPLEXITY_API_KEY = 'your-perplexity-key';
   export const EMBEDDING_API_KEY = 'your-openai-key';
   export const FIREBASE_HOSTING_URL = 'https://your-project-id.web.app';
   ```

4. **Build the Extension:**
   ```bash
   npm run build
   ```

5. **Load Extension in Chrome:**
   - Go to `chrome://extensions/`
   - Enable *Developer mode*
   - Click *Load unpacked* and select the `dist/` directory

## Usage

- **Sign In**: Click the extension icon and authenticate via Firebase.
- **Highlight Text**: Select text on any webpage for AI-powered insights.
- **Summarize Page**: Use the "Summarize" feature to get a concise overview of the current webpage.
- **Ask Anything**: Hover or click on any word or phrase to get a quick definition or ask for in-depth explanations via RAG.
- **View Graph**: Navigate to the *Graph* tab to see your knowledge graph.
- **Explore**: Zoom, drag, and hover over nodes.
- **Share**: Click "Share Graph" to generate a public link.

## Code Explanation

- `src/graph/`: Implements the D3.js-based graph.
- `src/popup/`: Contains the UI logic for the popup.
- `src/services/`: Handles API calls and Firebase interactions.
- `src/config.ts`: Centralized configuration for API keys and hosting URL.

## Links

- [GitHub Repository](https://github.com/iamaayushijain/perplexity-lens)
- [Live Demo (View Shared Graph)](https://youtu.be/SCPklDuSR3U)

## Limitations

- Large graphs may load slowly.
- Only selected concept metadata is shared; full text and browsing history remain private.
- Currently supported on Chromium-based browsers only.

---

> 🔐 **Privacy Note:** Your browsing history and full text content are never uploaded or shared. Only selected concepts and their relationships are used to build the graph.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- **Perplexity AI** for intelligent text explanations and summarization.
- **D3.js** for graph visualization.
- **Firebase** for authentication and hosting.
- **React**, **TypeScript**, and **TailwindCSS** for a modern frontend framework.

---

🚀 *Transform your daily reading into a meaningful visual map of knowledge with Perplexity Lens!*
