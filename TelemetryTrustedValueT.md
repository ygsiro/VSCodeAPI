# TelemetryTrustedValue<T>

A special value wrapper denoting a value that is safe to not clean. This is to be used when you can guarantee no identifiable information is contained in the value and the cleaning is improperly redacting it.

## Constructors

```typescript
new TelemetryTrustedValue<T>(value: T): TelemetryTrustedValue<T>
```

## Properties

### value

```typescript
value: T
```

