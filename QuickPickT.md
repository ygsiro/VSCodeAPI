## QuickPick&lt;T&gt;

A concrete QuickInput to let the user pick an item from a list of items of type T. The items can be filtered through a filter text field and there is an option canSelectMany to allow for selecting multiple items.

Note that in many cases the more convenient showQuickPick is easier to use. createQuickPick should be used when showQuickPick does not offer the required flexibility.

## Events

### onDidAccept

```typescript
onDidAccept: Event<void>
```

### onDidChangeActive

```typescript
onDidChangeActive: Event<readonly T[]>
```

### onDidChangeSelection

```typescript
onDidChangeSelection: Event<readonly T[]>
```

### onDidChangeValue

```typescript
onDidChangeValue: Event<string>
```

### onDidHide

```typescript
onDidHide: Event<void>
```

### onDidTriggerButton

```typescript
onDidTriggerButton: Event<QuickInputButton>
```

### onDidTriggerItemButton

```typescript
onDidTriggerItemButton: Event<QuickPickItemButtonEvent<T>>
```

## Properties

### activeItems

```typescript
activeItems: readonly T[]
```

### busy

```typescript
busy: boolean
```

### buttons

```typescript
buttons: readonly QuickInputButton[]
```

### canSelectMany

```typescript
canSelectMany: boolean
```

### enabled

```typescript
enabled: boolean
```

### ignoreFocusOut

```typescript
ignoreFocusOut: boolean
```

### items

```typescript
items: readonly T[]
```

### keepScrollPosition

```typescript
keepScrollPosition?: boolean
```

### matchOnDescription

```typescript
matchOnDescription: boolean
```

### matchOnDetail

```typescript
matchOnDetail: boolean
```

### placeholder

```typescript
placeholder: string
```

### selectedItems

```typescript
selectedItems: readonly T[]
```

### step

```typescript
step: number
```

### title

```typescript
title: string
```

### totalSteps

```typescript
totalSteps: number
```

### value

```typescript
value: string
```

## Methods

### dispose

```typescript
dispose(): void
```

### hide

```typescript
hide(): void
```

### show

```typescript
show(): void
```

[QuickPickItemButtonEvent]: QuickPickItemButtonEventT.md
[Event]: EventT.md
[QuickInputButton]: QuickInputButton.md
