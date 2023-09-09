# MarkdownString

Human-readable text that supports formatting via the markdown syntax.

Rendering of theme icons via the $(<name>)-syntax is supported when the supportThemeIcons is set to true.

Rendering of embedded html is supported when supportHtml is set to true.

## Constructors

```typescript
new MarkdownString(value?: string, supportThemeIcons?: boolean): MarkdownString
```

## Properties

### baseUri

```typescript
baseUri?: Uri
```

### isTrusted

```typescript
isTrusted?: boolean | {enabledCommands: readonly string[]}
```

### supportHtml

```typescript
supportHtml?: boolean
```

### supportThemeIcons

```typescript
supportThemeIcons?: boolean
```

### value

```typescript
value: string
```

## Methods

### appendCodeblock

```typescript
appendCodeblock(value: string, language?: string): MarkdownString
```

### appendMarkdown

```typescript
appendMarkdown(value: string): MarkdownString
```

### appendText

```typescript
appendText(value: string): MarkdownString
```

