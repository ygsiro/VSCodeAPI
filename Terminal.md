# Terminal

An individual terminal instance within the integrated terminal.

## Properties

### creationOptions

```typescript
creationOptions: Readonly<TerminalOptions | ExtensionTerminalOptions>
```

### exitStatus

```typescript
exitStatus: TerminalExitStatus
```

### name

```typescript
name: string
```

### processId

```typescript
processId: Thenable<number>
```

### state

```typescript
state: TerminalState
```

## Methods

### dispose

```typescript
dispose(): void
```

### hide

```typescript
hide(): void
```

### sendText

```typescript
sendText(text: string, addNewLine?: boolean): void
```

### show

```typescript
show(preserveFocus?: boolean): void
```

