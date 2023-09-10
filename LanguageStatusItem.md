# LanguageStatusItem

A language status item is the preferred way to present language status reports for the active text editors, such as selected linter or notifying about a configuration problem.

## Properties

### accessibilityInformation

```typescript
accessibilityInformation?: AccessibilityInformation
```

### busy

```typescript
busy: boolean
```

### command

```typescript
command: Command
```

### detail

```typescript
detail?: string
```

### id

```typescript
id: string
```

### name

```typescript
name: string
```

### selector

```typescript
selector: DocumentSelector
```

### severity

```typescript
severity: LanguageStatusSeverity
```

### text

```typescript
text: string
```

## Methods

### dispose

```typescript
dispose(): void
```

[LanguageStatusSeverity]: LanguageStatusSeverity.md
[AccessibilityInformation]: AccessibilityInformation.md
[Command]: Command.md
[DocumentSelector]: DocumentSelector.md
