# DebugAdapterTracker

A Debug Adapter Tracker is a means to track the communication between the editor and a Debug Adapter.

## Events

### onDidSendMessage

```typescript
onDidSendMessage(message: any): void
```

### onWillReceiveMessage

```typescript
onWillReceiveMessage(message: any): void
```

### onWillStartSession

```typescript
onWillStartSession(): void
```

### onWillStopSession

```typescript
onWillStopSession(): void
```

## Methods

### onError

```typescript
onError(error: Error): void
```

### onExit

```typescript
onExit(code: number, signal: string): void
```

