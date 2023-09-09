# GlobalEnvironmentVariableCollection

A collection of mutations that an extension can apply to a process environment. Applies to all scopes.

## Properties

### description

```typescript
description: string | MarkdownString
```

### persistent

```typescript
persistent: boolean
```

## Methods

### append

```typescript
append(variable: string, value: string, options?: EnvironmentVariableMutatorOptions): void
```

### clear

```typescript
clear(): void
```

### delete

```typescript
delete(variable: string): void
```

### forEach

```typescript
forEach(callback: (variable: string, mutator: EnvironmentVariableMutator, collection: EnvironmentVariableCollection) => any, thisArg?: any): void
```

### get

```typescript
get(variable: string): EnvironmentVariableMutator
```

### getScoped

```typescript
getScoped(scope: EnvironmentVariableScope): EnvironmentVariableCollection
```

### prepend

```typescript
prepend(variable: string, value: string, options?: EnvironmentVariableMutatorOptions): void
```

### replace

```typescript
replace(variable: string, value: string, options?: EnvironmentVariableMutatorOptions): void
```

