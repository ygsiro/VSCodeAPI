# TreeItem

## Constructors

```typescript
new TreeItem(label: string | TreeItemLabel, collapsibleState?: TreeItemCollapsibleState): TreeItem
```

```typescript
new TreeItem(resourceUri: Uri, collapsibleState?: TreeItemCollapsibleState): TreeItem
```

## Properties

### accessibilityInformation

```typescript
accessibilityInformation?: AccessibilityInformation
```

### checkboxState

```typescript
checkboxState?: TreeItemCheckboxState | {accessibilityInformation: AccessibilityInformation, state: TreeItemCheckboxState, tooltip: string}
```

### collapsibleState

```typescript
collapsibleState?: TreeItemCollapsibleState
```

### command

```typescript
command?: Command
```

### contextValue

```typescript
contextValue?: string
```

### description

```typescript
description?: string | boolean
```

### iconPath

```typescript
iconPath?: string | Uri | ThemeIcon | {dark: string | Uri, light: string | Uri}
```

### id

```typescript
id?: string
```

### label

```typescript
label?: string | TreeItemLabel
```

### resourceUri

```typescript
resourceUri?: Uri
```

### tooltip

```typescript
tooltip?: string | MarkdownString
```

[MarkdownString]: MarkdownString.md
[TreeItemCheckboxState]: TreeItemCheckboxState.md
[Uri]: Uri.md
[AccessibilityInformation]: AccessibilityInformation.md
[TreeItemLabel]: TreeItemLabel.md
[TreeItemCollapsibleState]: TreeItemCollapsibleState.md
[ThemeIcon]: ThemeIcon.md
[Command]: Command.md
