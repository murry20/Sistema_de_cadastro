import java.util.Scanner;

public class sistema_de_cadastro {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        // PRODUTOS
        String produto1 = "Notebook";
        String produto2 = "mouse";
        String produto3 = "Teclado";
        String produto4 = "Monitor";
        String produto5 = "Headset";

        // QUANTIDADE EM ESTOQUE
        int[] estoques = {10, 3, 0, 150, 200};

        // PREÇOS DE VENDA
        double[] precos = {3500.00, 120.00, 250.00, 900.00, 300.00};

        // ARRAYS PARA OS CÁLCULOS
        double[] valoresTotais = new double[5];
        double[] gastosTotais = new double[5];
        double[] lucrosTotais = new double[5];

        // Variáveis para somar o total da loja inteira
        double faturamentoTotalLoja = 0;
        double gastoTotalLoja = 0;
        double lucroTotalLoja = 0;

        // O "Loop" faz toda a matemática automaticamente
        for (int i = 0; i < 5; i++) {
            valoresTotais[i] = estoques[i] * precos[i];

            // Definindo que o custo (gasto) é de 40% do preço de venda
            gastosTotais[i] = valoresTotais[i] * 0.40;

            // Lucro bruto por produto
            lucrosTotais[i] = valoresTotais[i] - gastosTotais[i];

            // Somando nos totais gerais da loja
            faturamentoTotalLoja += valoresTotais[i];
            gastoTotalLoja += gastosTotais[i];
            lucroTotalLoja += lucrosTotais[i];
        }

        // RELATÓRIO
        System.out.println("===== RELATÓRIO DE ESTOQUE E FINANCEIRO =====");
        System.out.println();

        // PRODUTO 1
        System.out.println("Produto: " + produto1);
        System.out.println("Quantidade: " + estoques[0]);
        System.out.println("Preço de Venda: R$ " + precos[0]);
        System.out.println("Valor Total em Estoque: R$ " + valoresTotais[0]);
        System.out.println("Gastos (Custo): R$ " + gastosTotais[0]);
        System.out.println("Lucro Estimado: R$ " + lucrosTotais[0]);

        if (estoques[0] == 0) {
            System.out.println("Status: PRODUTO EM FALTA");
        } else if (estoques[0] <= 3) {
            System.out.println("Status: PRECISA DE REPOSIÇÃO");
        } else {
            System.out.println("Status: ESTOQUE OK");
        }
        System.out.println("----------------------------");

        // PRODUTO 2
        System.out.println("Produto: " + produto2);
        System.out.println("Quantidade: " + estoques[1]);
        System.out.println("Preço de Venda: R$ " + precos[1]);
        System.out.println("Valor Total em Estoque: R$ " + valoresTotais[1]);
        System.out.println("Gastos (Custo): R$ " + gastosTotais[1]);
        System.out.println("Lucro Estimado: R$ " + lucrosTotais[1]);

        if (estoques[1] == 0) {
            System.out.println("Status: PRODUTO EM FALTA");
        } else if (estoques[1] <= 3) {
            System.out.println("Status: PRECISA DE REPOSIÇÃO");
        } else {
            System.out.println("Status: ESTOQUE OK");
        }
        System.out.println("----------------------------");

        // PRODUTO 3
        System.out.println("Produto: " + produto3);
        System.out.println("Quantidade: " + estoques[2]);
        System.out.println("Preço de Venda: R$ " + precos[2]);
        System.out.println("Valor Total em Estoque: R$ " + valoresTotais[2]);
        System.out.println("Gastos (Custo): R$ " + gastosTotais[2]);
        System.out.println("Lucro Estimado: R$ " + lucrosTotais[2]);

        if (estoques[2] == 0) {
            System.out.println("Status: PRODUTO EM FALTA");
        } else if (estoques[2] <= 3) {
            System.out.println("Status: PRECISA DE REPOSIÇÃO");
        } else {
            System.out.println("Status: ESTOQUE OK");
        }
        System.out.println("----------------------------");

        // PRODUTO 4
        System.out.println("Produto: " + produto4);
        System.out.println("Quantidade: " + estoques[3]);
        System.out.println("Preço de Venda: R$ " + precos[3]);
        System.out.println("Valor Total em Estoque: R$ " + valoresTotais[3]);
        System.out.println("Gastos (Custo): R$ " + gastosTotais[3]);
        System.out.println("Lucro Estimado: R$ " + lucrosTotais[3]);

        if (estoques[3] == 0) {
            System.out.println("Status: PRODUTO EM FALTA");
        } else if (estoques[3] <= 3) {
            System.out.println("Status: PRECISA DE REPOSIÇÃO");
        } else {
            System.out.println("Status: ESTOQUE OK");
        }
        System.out.println("----------------------------");

        // PRODUTO 5
        System.out.println("Produto: " + produto5);
        System.out.println("Quantidade: " + estoques[4]);
        System.out.println("Preço de Venda: R$ " + precos[4]);
        System.out.println("Valor Total em Estoque: R$ " + valoresTotais[4]);
        System.out.println("Gastos (Custo): R$ " + gastosTotais[4]);
        System.out.println("Lucro Estimado: R$ " + lucrosTotais[4]);

        if (estoques[4] == 0) {
            System.out.println("Status: PRODUTO EM FALTA");
        } else if (estoques[4] <= 3) {
            System.out.println("Status: PRECISA DE REPOSIÇÃO");
        } else {
            System.out.println("Status: ESTOQUE OK");
        }
        System.out.println("----------------------------");

        // RESUMO GERAL DA LOJA
        System.out.println();
        System.out.println("===== BALANÇO GERAL DA LOJA =====");
        System.out.println("Valor Total do Estoque Atual: R$ " + faturamentoTotalLoja);
        System.out.println("Gasto Total de Aquisição: R$ " + gastoTotalLoja);
        System.out.println("Lucro Líquido Estimado: R$ " + lucroTotalLoja);
        System.out.println("=================================");
    }
}