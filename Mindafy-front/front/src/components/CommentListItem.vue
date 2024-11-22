<!-- CommentListItem.vue -->
<template>
    <div>
      <p> - {{ comment.content }}</p>
    </div>
</template>

<script setup>
    const props = defineProps({
    comment: Object,
    });
</script>

<style scoped>

</style>