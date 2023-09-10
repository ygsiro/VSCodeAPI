# TelemetryLogger

A telemetry logger which can be used by extensions to log usage and error telementry.

A logger wraps around an sender but it guarantees that

user settings to disable or tweak telemetry are respected, and that
potential sensitive data is removed
It also enables an "echo UI" that prints whatever data is send and it allows the editor to forward unhandled errors to the respective extensions.

To get an instance of a TelemetryLogger, use createTelemetryLogger.

## Events

### onDidChangeEnableStates

```typescript
onDidChangeEnableStates: Event<TelemetryLogger>
```

## Properties

### isErrorsEnabled

```typescript
isErrorsEnabled: boolean
```

### isUsageEnabled

```typescript
isUsageEnabled: boolean
```

## Methods

### dispose

```typescript
dispose(): void
```

### logError

```typescript
logError(eventName: string, data?: Record<string, any>): void
```

### logError

```typescript
logError(error: Error, data?: Record<string, any>): void
```

### logUsage

```typescript
logUsage(eventName: string, data?: Record<string, any>): void
```

[Event]: EventT.md
