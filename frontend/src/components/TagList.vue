<script setup lang="ts">
    import {ref, watchEffect} from 'vue';
    import {API} from '../globals';
    import type {Ref} from 'vue'
    import AddTag from './AddTag.vue';

    const props = defineProps<{
        onClick?: (_val: any) => void
    }>()
    
    const tags: Ref<Array<any>> = ref([])

    function getTags(){
        fetch(API + "tags/")
            .then((response) => {
                if(response.ok){
                    response.json()
                        .then((v) => tags.value = v).then(() => console.log(tags))
                }else{
                    alert('Could not get tags')
                }
            })
    }

    watchEffect(() => {
        getTags()
    })
</script>

<template>
    <v-row>
        <v-chip 
            v-for="tag in tags"
            label
            @click="$props.onClick !== undefined ? $props.onClick(tag) : null"
            >
            {{tag.name}} ({{tag.orders.length}})
        </v-chip>
        <AddTag :on-add="getTags"/>
    </v-row>
</template>

<style scoped>
    .v-chip{
        margin: 5px;
    }
</style>