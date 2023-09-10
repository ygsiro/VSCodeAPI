# InputBox

A concrete QuickInput to let the user input a text value.

Note that in many cases the more convenient showInputBox is easier to use. createInputBox should be used when showInputBox does not offer the required flexibility.

## Events

### onDidAccept

```typescript
onDidAccept: Event<void>
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

## Properties

### busy

```typescript
busy: boolean
```

### buttons

```typescript
buttons: readonly QuickInputButton[]
```

### enabled

```typescript
enabled: boolean
```

### ignoreFocusOut

```typescript
ignoreFocusOut: boolean
```

### password

```typescript
password: boolean
```

### placeholder

```typescript
placeholder: string
```

### prompt

```typescript
prompt: string
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

### validationMessage

```typescript
validationMessage: string | InputBoxValidationMessage
```

### value

```typescript
value: string
```

### valueSelection

```typescript
valueSelection: readonly [number, number]
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

[InputBoxValidationMessage]: InputBoxValidationMessage.md
[Event]: EventT.md
[QuickInputButton]: QuickInputButton.md
