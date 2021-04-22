<template>
    <div class="about" style="font-size:large;">
        DrEYEve is an application that converts driving data collected through car sensors into real-time behavioural profiles. This is achieved by using state of the art AI techniques in order to evaluate the data collected during a driving trip. DrEYEve not only offers real-time monitoring of driver behaviour but it also allows analysing behavioural patterns observed on already carried out routes. Our mission is to help drivers improve their driving performance through the driving profiles generated for each one of them. DrEYEve focuses on tracking driving aggressiveness and informs the driver when such a behaviour is present. This will help the driver evaluate his driving behaviour, learn from his mistakes and eventually adopt a more eco-friendly and safer driving behaviour.
    </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';

@Component({
    name: 'About'
})
export default class About extends Vue {}
</script>