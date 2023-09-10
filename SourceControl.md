# SourceControl

An source control is able to provide resource states to the editor and interact with the editor in several source control related ways.

## Properties

### acceptInputCommand

```typescript
acceptInputCommand?: Command
```

### commitTemplate

```typescript
commitTemplate?: string
```

### count

```typescript
count?: number
```

### id

```typescript
id: string
```

### inputBox

```typescript
inputBox: SourceControlInputBox
```

### label

```typescript
label: string
```

### quickDiffProvider

```typescript
quickDiffProvider?: QuickDiffProvider
```

### rootUri

```typescript
rootUri: Uri
```

### statusBarCommands

```typescript
statusBarCommands?: Command[]
```

## Methods

### createResourceGroup

```typescript
createResourceGroup(id: string, label: string): SourceControlResourceGroup
```

### dispose

```typescript
dispose(): void
```

[SourceControlInputBox]: SourceControlInputBox.md
[Uri]: Uri.md
[QuickDiffProvider]: QuickDiffProvider.md
[SourceControlResourceGroup]: SourceControlResourceGroup.md
[Command]: Command.md
