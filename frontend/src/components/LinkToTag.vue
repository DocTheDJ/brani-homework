<script setup lang="ts">
    import { API } from '@/globals';
    import { ref } from 'vue';
    import TagList from './TagList.vue';

    const props = defineProps<{
        onAdd: () => void,
        item: any
    }>()

    const dialog = ref(false)

    function link(_val: any){
        const options = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ order_id: props.item.id, tag_id: _val.id })
        }
        fetch(API + "link/", options)
            .then((response) => {
                if(!response.ok){
                    alert('Linking failed')
                }else{
                    props.onAdd();
                    close();
                }
            })
    }
    function close(){
        dialog.value = false
    }
</script>

<template>
    <v-dialog
        v-model="dialog"
        max-width="500px"
    >
        <template v-slot:activator="{props}">
            <v-btn
                class="mb-2"
                color="primary"
                variant="elevated"
                v-bind="props"
            >
                AddTag
            </v-btn>
        </template>
        <v-card>
            <v-card-title>
                <span class="text-h5">Choose tag to add for {{ $props.item.email }}</span>
            </v-card-title>
            
            <v-card-text>
                <TagList :on-click="link"/>
            </v-card-text>
            
            <v-card-actions></v-card-actions>
        </v-card>

    </v-dialog>
</template>