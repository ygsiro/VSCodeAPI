# InputBoxOptions

Options to configure the behavior of the input box UI.

## Properties

### ignoreFocusOut

```typescript
ignoreFocusOut?: boolean
```

### password

```typescript
password?: boolean
```

### placeHolder

```typescript
placeHolder?: string
```

### prompt

```typescript
prompt?: string
```

### title

```typescript
title?: string
```

### value

```typescript
value?: string
```

### valueSelection

```typescript
valueSelection?: [number, number]
```

## Methods

### validateInput

```typescript
validateInput(value: string): string | InputBoxValidationMessage | Thenable<string | InputBoxValidationMessage>
```

[InputBoxValidationMessage]: InputBoxValidationMessage.md
