<script lang="ts">
  import { onMount } from "svelte";
  import DatasetRow from './lib/DatasetRow.svelte'

  interface Dataset {
    id: number;
    name: string;
    publisher: string;
    source: string | null;
    description: string;
  }

  let datasets: Array<Dataset> = $state([]);

  onMount(async function () {
    const response = await fetch('/api/datasets');
    const data: Array<Dataset> = await response.json();
    data.forEach(dataset => {
      datasets.push(dataset);
    });
  });
</script>

<main>
    <h1>Open Data</h1>

    {#each datasets as dataset}
      <DatasetRow
        id={dataset.id}
        name={dataset.name}
        publisher={dataset.publisher}
        source={dataset.source}
        description={dataset.description}
      />
    {/each}

    <hr>

    <a href="/docs" id="api-ref">API Reference</a>
</main>

<style>
  #api-ref {
    display: block;
    margin-top: 1em;
  }
</style>
