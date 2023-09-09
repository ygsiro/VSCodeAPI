# TelemetrySender

The telemetry sender is the contract between a telemetry logger and some telemetry service. Note that extensions must NOT call the methods of their sender directly as the logger provides extra guards and cleaning.

```typescript
const sender: vscode.TelemetrySender = {...};
const logger = vscode.env.createTelemetryLogger(sender);

// GOOD - uses the logger
logger.logUsage('myEvent', { myData: 'myValue' });

// BAD - uses the sender directly: no data cleansing, ignores user settings, no echoing to the telemetry output channel etc
sender.logEvent('myEvent', { myData: 'myValue' });
```

## Methods

### flush

```typescript
flush(): void | Thenable<void>
```

### sendErrorData

```typescript
sendErrorData(error: Error, data?: Record<string, any>): void
```

### sendEventData

```typescript
sendEventData(eventName: string, data?: Record<string, any>): void
```

