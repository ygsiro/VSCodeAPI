# DebugConfigurationProvider

A debug configuration provider allows to add debug configurations to the debug service and to resolve launch configurations before they are used to start a debug session. A debug configuration provider is registered via registerDebugConfigurationProvider.

## Methods

### provideDebugConfigurations

```typescript
provideDebugConfigurations(folder: WorkspaceFolder, token?: CancellationToken): ProviderResult<DebugConfiguration[]>
```

### resolveDebugConfiguration

```typescript
resolveDebugConfiguration(folder: WorkspaceFolder, debugConfiguration: DebugConfiguration, token?: CancellationToken): ProviderResult<DebugConfiguration>
```

### resolveDebugConfigurationWithSubstitutedVariables

```typescript
resolveDebugConfigurationWithSubstitutedVariables(folder: WorkspaceFolder, debugConfiguration: DebugConfiguration, token?: CancellationToken): ProviderResult<DebugConfiguration>
```

[WorkspaceFolder]: WorkspaceFolder.md
[DebugConfiguration]: DebugConfiguration.md
[ProviderResult]: ProviderResultT.md
[CancellationToken]: CancellationToken.md
