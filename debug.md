# debug

Namespace for debug functionality.

## Variables

### activeDebugConsole

```typescript
activeDebugConsole: DebugConsole
```

### activeDebugSession

```typescript
activeDebugSession: DebugSession | undefined
```

### breakpoints

```typescript
breakpoints: readonly Breakpoint[]
```

## Events

### onDidChangeActiveDebugSession

```typescript
onDidChangeActiveDebugSession: Event<DebugSession | undefined>
```

### onDidChangeBreakpoints

```typescript
onDidChangeBreakpoints: Event<BreakpointsChangeEvent>
```

### onDidReceiveDebugSessionCustomEvent

```typescript
onDidReceiveDebugSessionCustomEvent: Event<DebugSessionCustomEvent>
```

### onDidStartDebugSession

```typescript
onDidStartDebugSession: Event<DebugSession>
```

### onDidTerminateDebugSession

```typescript
onDidTerminateDebugSession: Event<DebugSession>
```

## Functions

### addBreakpoints

```typescript
addBreakpoints(breakpoints: readonly Breakpoint[]): void
```

### asDebugSourceUri

```typescript
asDebugSourceUri(source: DebugProtocolSource, session?: DebugSession): Uri
```

### registerDebugAdapterDescriptorFactory

```typescript
registerDebugAdapterDescriptorFactory(debugType: string, factory: DebugAdapterDescriptorFactory): Disposable
```

### registerDebugAdapterTrackerFactory

```typescript
registerDebugAdapterTrackerFactory(debugType: string, factory: DebugAdapterTrackerFactory): Disposable
```

### registerDebugConfigurationProvider

```typescript
registerDebugConfigurationProvider(debugType: string, provider: DebugConfigurationProvider, triggerKind?: DebugConfigurationProviderTriggerKind): Disposable
```

### removeBreakpoints

```typescript
removeBreakpoints(breakpoints: readonly Breakpoint[]): void
```

### startDebugging

```typescript
startDebugging(folder: WorkspaceFolder, nameOrConfiguration: string | DebugConfiguration, parentSessionOrOptions?: DebugSession | DebugSessionOptions): Thenable<boolean>
```

### stopDebugging

```typescript
stopDebugging(session?: DebugSession): Thenable<void>
```

