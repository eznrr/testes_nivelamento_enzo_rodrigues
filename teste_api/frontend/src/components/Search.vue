<template>
    <div class="container mt-5">
        <h2 class="text-center text-uppercase mb-4">buscar operadoras</h2>
        <div class="input-group mb-4">
            <input v-model="termoBusca" type="text" class="form-control" placeholder="Digite o nome da operadora...">
            <button @click="buscar" class="btn btn-primary">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                    <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/>
                </svg> Buscar
            </button>
        </div>

        <div v-if="resultado.length">
            <ul class="list-group mb-5">
                <li v-for="operadora in resultado" :key="operadora.Registro_ANS" class="list-group-item mb-2">
                    <h4><strong>{{ operadora.Nome_Fantasia || operadora.Razao_Social }}</strong></h4>
                    <p><strong>Razão Social:</strong> {{ operadora.Razao_Social || "Não informado" }}</p>
                    <p><strong>Cidade:</strong> {{ operadora.Cidade || "Não informado" }}</p>
                    <p><strong>UF:</strong> {{ operadora.UF || "Não informado" }}</p>
                    <p><strong>CNPJ:</strong> {{ operadora.CNPJ || "Não informado" }}</p>
                    <p><strong>Registro ANS:</strong> {{ operadora.Registro_ANS || "Não informado" }}</p>
                    <p><strong>Modalidade:</strong> {{ operadora.Modalidade || "Não informado" }}</p>
                </li>
            </ul>
        </div>

        <div v-else-if="buscou" class="alert alert-warning mt-3">
            Nenhum resultado encontrado.
        </div>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        data() {
            return {
                termoBusca: "",
                resultado: [],
                buscou: false,
            };
        },
        methods: {
            async buscar() {
                if (!this.termoBusca) return;
                try {
                    const response = await axios.get(`http://127.0.0.1:5000/buscar?nome=${this.termoBusca}`);
                    this.resultado = response.data;
                } catch (error) {
                    console.error("Erro na busca:", error);
                    this.resultado = [];
                }
                this.buscou = true;
            },
        },
    };
</script>
  
<style>
    body {
        background-color: #e2e8ec;
    }
</style>