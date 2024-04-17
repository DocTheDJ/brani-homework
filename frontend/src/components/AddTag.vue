<script setup lang="ts">
    import { API } from '@/globals';
    import { ref, watch } from 'vue';

    //define properties for component
    const props = defineProps<{
        onAdd: () => void
    }>()

    //set state
    const newName = ref("")
    const dialog = ref(false)

    //save function
    function save(){
        const options = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name: newName.value })
        }
        fetch(API + "tags/", options)
            .then((response) => {
                if(!response.ok){
                    alert('Tag creation failed !')
                }else{
                    response.json()
                        .then(props.onAdd)
                        .then(close)
                }
            })
    }

    watch(dialog, (new_val) => {
        if(!new_val) newName.value = ""
    })

    function close(){
        dialog.value = false
    }
</script>

<template>
    <v-dialog
        v-model="dialog"
        max-width="500px"
    >
        <!-- open button -->
        <template v-slot:activator="{props}">
            <v-btn
                class="mb-2"
                color="primary"
                variant="elevated"
                v-bind="props"
            >
                New Tag
            </v-btn>
        </template>
        <!-- modal -->
        <v-card>
                <!-- header -->
                <v-card-title>
                    <span class="text-h5">New Tag</span>
                </v-card-title>
                <!-- content -->
                <v-card-text>
                    <v-container>
                        <v-row>
                            <v-text-field
                                v-model="newName"
                                label="Name"
                            ></v-text-field>
                        </v-row>
                    </v-container>
                </v-card-text>

                <!-- actions -->
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                        color="blue-darken-1"
                        variant="text"
                        @click="close"
                    >
                        Cancel
                    </v-btn>
                    <v-btn
                        color="blue-darken-1"
                        variant="text"
                        @click="save"
                    >
                        Save
                    </v-btn>
                </v-card-actions>
            </v-card>
    </v-dialog>
</template>