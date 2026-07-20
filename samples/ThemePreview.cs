using System.Collections.Immutable;
using System.Diagnostics.CodeAnalysis;

namespace Acuity.ThemePreview;

/// <summary>
/// Exercises common C# syntax categories for visual inspection.
/// Comments should remain readable but visibly subordinate to executable code.
/// </summary>
[SuppressMessage("Style", "IDE0058", Justification = "Theme preview only")]
public sealed record ThemeSample<T>(Guid Id, string Name, T Value)
    where T : notnull
{
    private const int MaximumAttempts = 3;
    private static readonly TimeSpan Timeout = TimeSpan.FromSeconds(2.5);

    public async Task<ImmutableArray<string>> FormatAsync(
        IEnumerable<T> values,
        CancellationToken cancellationToken = default)
    {
        ArgumentNullException.ThrowIfNull(values);

        var results = ImmutableArray.CreateBuilder<string>();
        var attempt = 0;

        while (attempt++ < MaximumAttempts)
        {
            try
            {
                foreach (var item in values.Where(static x => x is not null))
                {
                    cancellationToken.ThrowIfCancellationRequested();
                    results.Add($"{Name}: {item} @ {DateTimeOffset.UtcNow:O}");
                }

                await Task.Delay(Timeout, cancellationToken).ConfigureAwait(false);
                return results.ToImmutable();
            }
            catch (OperationCanceledException) when (cancellationToken.IsCancellationRequested)
            {
                throw;
            }
            catch (Exception exception)
            {
                Console.Error.WriteLine($"Attempt {attempt} failed: {exception.Message}");
            }
        }

        return [];
    }
}
