# TabGroups

Represents the main editor area which consists of multiple groups which contain tabs.

## Events

### onDidChangeTabGroups

```typescript
onDidChangeTabGroups: Event<TabGroupChangeEvent>
```

### onDidChangeTabs

```typescript
onDidChangeTabs: Event<TabChangeEvent>
```

## Properties

### activeTabGroup

```typescript
activeTabGroup: TabGroup
```

### all

```typescript
all: readonly TabGroup[]
```

## Methods

### close

```typescript
close(tab: Tab | readonly Tab[], preserveFocus?: boolean): Thenable<boolean>
```

### close

```typescript
close(tabGroup: TabGroup | readonly TabGroup[], preserveFocus?: boolean): Thenable<boolean>
```

[TabChangeEvent]: TabChangeEvent.md
[TabGroupChangeEvent]: TabGroupChangeEvent.md
[Event]: EventT.md
[TabGroup]: TabGroup.md
[Tab]: Tab.md
