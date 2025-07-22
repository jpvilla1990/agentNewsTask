# agentNewsTask

## Concept

### Essential

<pre lang="text"><code>
┌─────────────┐
│  Searcher   │────▶ https://app.tavily.com/home
└─────┬───────┘
      │
      ▼
┌──────────────┐
│   Scraper    │────▶ https://dashboard.scrape.do/
└─────┬────────┘
      ▼
┌──────────────┐
│ Summarizer?  │────▶ OpenAI / Local LLM (optional)
└─────┬────────┘
      ▼
┌──────────────────────┐
│  HTML Generator      │────▶ Formats newsletter
└─────┬────────────────┘
      ▼
┌─────────────┐
│ Mail Sender │────▶ Gmail / Mailgun / SMTP
└─────┬───────┘
      ▼
┌─────────────────────┐
│ Subscriber List     │────▶ Flat file or DB
└─────────────────────┘
</code></pre>
