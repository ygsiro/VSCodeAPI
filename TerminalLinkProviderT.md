# TerminalLinkProvider<T>

A provider that enables detection and handling of links within terminals.

## Methods

### handleTerminalLink

```typescript
handleTerminalLink(link: T): ProviderResult<void>
```

### provideTerminalLinks

```typescript
provideTerminalLinks(context: TerminalLinkContext, token: CancellationToken): ProviderResult<T[]>
```

