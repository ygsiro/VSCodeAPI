# DebugAdapter

A debug adapter that implements the Debug Adapter Protocol can be registered with the editor if it implements the DebugAdapter interface.

## Events

### onDidSendMessage

```typescript
onDidSendMessage: Event<DebugProtocolMessage>
```

## Methods

### dispose

```typescript
dispose(): any
```

### handleMessage

```typescript
handleMessage(message: DebugProtocolMessage): void
```

[Event]: EventT.md
[DebugProtocolMessage]: DebugProtocolMessage.md
