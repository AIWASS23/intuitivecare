<template>
  <div id="app">
    <h1>Busca de Operadora</h1>
    <input v-model="cnpj" type="text" placeholder="Digite o CNPJ da operadora" />
    <button @click="buscarOperadora">Buscar</button>

    <div v-if="errorMessage" class="error">{{ errorMessage }}</div>

    <div v-if="operadora">
      <h3>{{ operadora.razao_social }} ({{ operadora.cnpj }})</h3>
      <p><strong>Nome Fantasia:</strong> {{ operadora.nome_fantasia }}</p>
      <p><strong>Modalidade:</strong> {{ operadora.modalidade }}</p>
      <p><strong>Endereço:</strong> {{ operadora.logradouro }}, {{ operadora.numero }} - {{ operadora.bairro }}</p>
      <p><strong>Telefone:</strong> {{ operadora.telefone }}</p>
      <p><strong>Representante:</strong> {{ operadora.representante }} - {{ operadora.cargo_representante }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      cnpj: '',
      operadora: null,
      errorMessage: '',
    };
  },
  methods: {
    async buscarOperadora() {
      if (!this.cnpj) {
        this.errorMessage = 'Por favor, forneça um CNPJ válido.';
        this.operadora = null;
        return;
      }

      try {
        const response = await axios.get(`http://127.0.0.1:8000/operadora/${this.cnpj}`);
        this.operadora = response.data;
        this.errorMessage = '';
      } catch (error) {
        this.errorMessage = 'Operadora não encontrada.';
        this.operadora = null;
      }
    },
  },
};
</script>

<style>
#errorMessage {
  color: red;
  font-weight: bold;
}
</style>
