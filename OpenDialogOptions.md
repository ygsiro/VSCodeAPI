# OpenDialogOptions

Options to configure the behaviour of a file open dialog.

Note 1: On Windows and Linux, a file dialog cannot be both a file selector and a folder selector, so if you set both canSelectFiles and canSelectFolders to true on these platforms, a folder selector will be shown.
Note 2: Explicitly setting canSelectFiles and canSelectFolders to false is futile and the editor then silently adjusts the options to select files.

## Properties

### canSelectFiles

```typescript
canSelectFiles?: boolean
```

### canSelectFolders

```typescript
canSelectFolders?: boolean
```

### canSelectMany

```typescript
canSelectMany?: boolean
```

### defaultUri

```typescript
defaultUri?: Uri
```

### filters

```typescript
filters?:
```

### openLabel

```typescript
openLabel?: string
```

### title

```typescript
title?: string
```

[Uri]: Uri.md
