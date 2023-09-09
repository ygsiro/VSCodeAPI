# ThemeIcon

A reference to a named icon. Currently, File, Folder, and ThemeIcon ids are supported. Using a theme icon is preferred over a custom icon as it gives product theme authors the possibility to change the icons.

Note that theme icons can also be rendered inside labels and descriptions. Places that support theme icons spell this out and they use the $(<name>)-syntax, for instance quickPick.label = "Hello World $(globe)".

## Static

### File

```typescript
File: ThemeIcon
```

### Folder

```typescript
Folder: ThemeIcon
```

## Constructors

```typescript
new ThemeIcon(id: string, color?: ThemeColor): ThemeIcon
```

## Properties

### color

```typescript
color?: ThemeColor
```

### id

```typescript
id: string
```

