<script setup lang="ts">
  import { ref, watchEffect } from 'vue'
  import type { Ref } from 'vue'
  import AddOrder from './AddOrder.vue'
  import {API} from '../globals';
  import LinkToTag from './LinkToTag.vue';
  import moment from 'moment';

  //state list of order
  const data: Ref<Array<any>> = ref([]);

  // order getting function
  function refresh(){
    fetch(API + "orders/").then((result) => {
      if(result.ok){
        result.json().then((v) => data.value = v)
      }else{
        alert('Something went wrong during API call.')
      }
    })
  }

  //remove tag function
  function removeTagLink(order: any, tag: any){
    const options = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ order: order, tag: tag })
    }
    fetch(API + "delink/", options)
      .then((response) => {
        if(response.ok){
          refresh()
        }else{
          alert('Failed to delink')
        }
      })
  }

  //format date
  function getDate(date: any){
    if(date == null) return "YYYY-MM-DD";
    return moment(date).format("YYYY-MM-DD")
  }

  //useEffect, onrender
  watchEffect(() => {
    refresh()
  })
</script>

<template>
  <!-- render rows, map based on data -->
    <v-row v-for="item in data">
      <!-- id column -->
        <v-col :cols="1">
          <v-sheet class="pa-2 ma-2">
            {{item.id}}
          </v-sheet>
        </v-col>
        <!-- email column -->
        <v-col :cols="4">
          <v-sheet class="pa-2 ma-2">
            {{item.email}}
          </v-sheet>
        </v-col>
        <!-- date column -->
        <v-col cols="auto">
          <v-sheet class="pa-2 ma-2">
            {{getDate(item.created)}}
          </v-sheet>
        </v-col>
        <!-- tags column -->
        <v-col>
          <v-sheet class="pa-2 ma-2">
            <v-chip
                class="ma-2"
                color="pink" 
                v-for="tag in item.tags"
                label
                prepend-icon="mdi-label"
                @click="() => removeTagLink(item, tag.tag)"
            >
            {{tag.tag.name}}
            </v-chip>
            <!-- linking modal -->
            <LinkToTag :on-add="refresh" :item="item"/>
          </v-sheet>
        </v-col>
    </v-row>
    <!-- add order modal -->
    <AddOrder :on-add="refresh"/>
</template>