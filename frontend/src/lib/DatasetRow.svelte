<script>
  export let id;
  export let name;
  export let publisher;
  export let source;
  export let description;
</script>

<div class="dataset-row">
    <h2>{name}</h2>

    {#if source}
    <small>Published by <a href={source} target="_blank">{publisher}</a></small>
    {:else}
    <small>Published by {publisher}</small>
    {/if}

    <p>{description}</p>

    <a href="/api/datasets/{id}/json">
    <button>{'{}'} JSON</button>
    </a>

    <a href="/api/datasets/{id}/csv">
    <button>☷ CSV</button>
    </a>
</div>

<style>
  .dataset-row {
    display: block;
    margin-bottom: 1em;
    text-align: left;
  }
</style>