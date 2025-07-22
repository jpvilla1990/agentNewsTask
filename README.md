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

### Scrapper

https://github.com/assafelovic/gpt-researcher

### TAVILY
https://app.tavily.com/
```bash
curl -X POST 'https://api.tavily.com/search' -H 'Content-Type:application/json' -H 'Authorization: Bearer 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' -d '{"query":"Last News AI Agents"}'
```