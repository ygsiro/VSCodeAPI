# SnippetString

A snippet string is a template which allows to insert text and to control the editor cursor when insertion happens.

A snippet can define tab stops and placeholders with $1, $2 and ${3:foo}. $0 defines the final tab stop, it defaults to the end of the snippet. Variables are defined with $name and ${name:default value}. Also see the full snippet syntax.

## Constructors

```typescript
new SnippetString(value?: string): SnippetString
```

## Properties

### value

```typescript
value: string
```

## Methods

### appendChoice

```typescript
appendChoice(values: readonly string[], number?: number): SnippetString
```

### appendPlaceholder

```typescript
appendPlaceholder(value: string | (snippet: SnippetString) => any, number?: number): SnippetString
```

### appendTabstop

```typescript
appendTabstop(number?: number): SnippetString
```

### appendText

```typescript
appendText(string: string): SnippetString
```

### appendVariable

```typescript
appendVariable(name: string, defaultValue: string | (snippet: SnippetString) => any): SnippetString
```

