# env

Namespace describing the environment the editor runs in.

## Variables

### appHost

```typescript
appHost: string
```

### appName

```typescript
appName: string
```

### appRoot

```typescript
appRoot: string
```

### clipboard

```typescript
clipboard: Clipboard
```

### isNewAppInstall

```typescript
isNewAppInstall: boolean
```

### isTelemetryEnabled

```typescript
isTelemetryEnabled: boolean
```

### language

```typescript
language: string
```

### logLevel

```typescript
logLevel: LogLevel
```

### machineId

```typescript
machineId: string
```

### remoteName

```typescript
remoteName: string | undefined
```

### sessionId

```typescript
sessionId: string
```

### shell

```typescript
shell: string
```

### uiKind

```typescript
uiKind: UIKind
```

### uriScheme

```typescript
uriScheme: string
```

## Events

### onDidChangeLogLevel

```typescript
onDidChangeLogLevel: Event<LogLevel>
```

### onDidChangeTelemetryEnabled

```typescript
onDidChangeTelemetryEnabled: Event<boolean>
```

## Functions

### asExternalUri

```typescript
asExternalUri(target: Uri): Thenable<Uri>
```

### createTelemetryLogger

```typescript
createTelemetryLogger(sender: TelemetrySender, options?: TelemetryLoggerOptions): TelemetryLogger
```

### openExternal

```typescript
openExternal(target: Uri): Thenable<boolean>
```

[Clipboard]: Clipboard.md
[Uri]: Uri.md
[UIKind]: UIKind.md
[TelemetrySender]: TelemetrySender.md
[Event]: EventT.md
[TelemetryLogger]: TelemetryLogger.md
[TelemetryLoggerOptions]: TelemetryLoggerOptions.md
[LogLevel]: LogLevel.md
