# AccessibilityInformation

Accessibility information which controls screen reader behavior.

## Properties

### label

```typescript
label: string
```

Label to be read out by a screen reader once the item has focus.

### role

```typescript
role?: string
```

Role of the widget which defines how a screen reader interacts with it.
The role should be set in special cases when for example a tree-like element behaves like a checkbox.
If role is not specified the editor will pick the appropriate role automatically.
More about aria roles can be found here <https://w3c.github.io/aria/#widget_roles>