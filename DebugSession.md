# DebugSession

A debug session.

## Properties

### configuration

```typescript
configuration: DebugConfiguration
```

### id

```typescript
id: string
```

### name

```typescript
name: string
```

### parentSession

```typescript
parentSession?: DebugSession
```

### type

```typescript
type: string
```

### workspaceFolder

```typescript
workspaceFolder: WorkspaceFolder
```

## Methods

### customRequest

```typescript
customRequest(command: string, args?: any): Thenable<any>
```

### getDebugProtocolBreakpoint

```typescript
getDebugProtocolBreakpoint(breakpoint: Breakpoint): Thenable<DebugProtocolBreakpoint>
```

[DebugConfiguration]: DebugConfiguration.md
[WorkspaceFolder]: WorkspaceFolder.md
[Breakpoint]: Breakpoint.md
[DebugProtocolBreakpoint]: DebugProtocolBreakpoint.md
