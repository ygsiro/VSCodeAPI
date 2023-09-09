# FoldingRangeKind

An enumeration of specific folding range kinds. The kind is an optional field of a FoldingRange and is used to distinguish specific folding ranges such as ranges originated from comments. The kind is used by commands like Fold all comments or Fold all regions. If the kind is not set on the range, the range originated from a syntax element other than comments, imports or region markers.

