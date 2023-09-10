# QuickInput

A light-weight user input UI that is initially not visible. After configuring it through its properties the extension can make it visible by calling show.

There are several reasons why this UI might have to be hidden and the extension will be notified through onDidHide. (Examples include: an explicit call to hide, the user pressing Esc, some other input UI opening, etc.)

A user pressing Enter or some other gesture implying acceptance of the current state does not automatically hide this UI component. It is up to the extension to decide whether to accept the user's input and if the UI should indeed be hidden through a call to hide.

When the extension no longer needs this input UI, it should dispose it to allow for freeing up any resources associated with it.

See QuickPick and InputBox for concrete UIs.

## Events

### onDidHide

```typescript
onDidHide: Event<void>
```

## Properties

### busy

```typescript
busy: boolean
```

### enabled

```typescript
enabled: boolean
```

### ignoreFocusOut

```typescript
ignoreFocusOut: boolean
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

[Event]: EventT.md
