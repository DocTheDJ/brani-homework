<script setup lang="ts">
    import { API } from '@/globals';
    import { ref, watch } from 'vue'

    // props for for the component
    const props = defineProps<{
        onAdd: () => void,
    }>()

    //states
    const newName = ref("")
    const dialog = ref(false)

    // save function
    function save(){
        //declare options for fetch
        const options = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email: newName.value })
        }
        //fetch to api
        fetch(API + "orders/", options)
            .then((response) => {
                //then check for failure
                if(!response.ok){
                    alert('Order creation failed !');
                }else{
                    //if ok then refresh and close
                    response.json()
                        .then(props.onAdd)
                        .then(close)
                }
            })
    }

    //watch for changes in opened modal/dialog
    watch(dialog, (new_val) => {
        if(!new_val){
            newName.value = "";
        }
    })

    function close(){
        dialog.value = false;
    }
</script>

<!-- basically a modal for adding orders -->

<template>
    <v-dialog
        v-model="dialog"
        max-width="500px"
    >
        <!-- basically just a button that opnes the dilaog -->
        <template v-slot:activator="{ props }">
            <v-btn
                class="mb-2"
                color="primary"
                dark
                v-bind="props"
            >
                New Item
            </v-btn>
        </template>
        <!-- dialog itself -->
        <v-card>
            <!-- header -->
            <v-card-title>
                <span class="text-h5">New Order</span>
            </v-card-title>

            <!-- body -->
            <v-card-text>
                <v-container>
                    <v-row>
                        <!-- fill email -->
                        <v-text-field
                            v-model="newName"
                            label="Email"
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