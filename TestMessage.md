# TestMessage

Message associated with the test state. Can be linked to a specific source range -- useful for assertion failures, for example.

## Static

### diff

```typescript
diff(message: string | MarkdownString, expected: string, actual: string): TestMessage
```

## Constructors

```typescript
new TestMessage(message: string | MarkdownString): TestMessage
```

## Properties

### actualOutput

```typescript
actualOutput?: string
```

### expectedOutput

```typescript
expectedOutput?: string
```

### location

```typescript
location?: Location
```

### message

```typescript
message: string | MarkdownString
```

