# agentNewsTask

## Concept

### Essential

<pre lang="text"><code>
┌─────────────┐
│  Scheduler  │────▶ Every week
└─────┬───────┘
      │
      ▼
┌──────────────┐
│   Scraper    │────▶ aiagentsdirectory.com
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
curl -X POST 'https://api.tavily.com/search' -H 'Content-Type:application/json' -H 'Authorization: Bearer TOKEN' -d '{"query":"Last News AI Agents"}'
```