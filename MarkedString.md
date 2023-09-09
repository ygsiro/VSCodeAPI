# MarkedString

MarkedString can be used to render human-readable text. It is either a markdown string or a code-block that provides a language and a code snippet. Note that markdown strings will be sanitized - that means html will be escaped.

deprecated - This type is deprecated, please use MarkdownString instead.
MarkedString: string | {language: string, value: string}

## Memento

### A

```typescript
A memento represents a storage utility. It can store and retrieve values.
```

## Methods

### get

```typescript
get<T>(key: string): T
```

### get

```typescript
get<T>(key: string, defaultValue: T): T
```

### keys

```typescript
keys(): readonly string[]
```

### update

```typescript
update(key: string, value: any): Thenable<void>
```

