-- Top 10 Operadoras com Maiores Despesas no Último Ano

SELECT 
    o.registro_ans, 
    o.razao_social, 
    SUM(d.vl_saldo_final) AS total_despesas
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras o ON d.reg_ans = o.registro_ans
WHERE 
    d.descricao ILIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    AND d.data >= (CURRENT_DATE - INTERVAL '1 year') 
GROUP BY 
    o.registro_ans, o.razao_social
ORDER BY 
    total_despesas DESC
LIMIT 10;

/*

registro_ans |                       razao_social                       | total_despesas 
--------------+----------------------------------------------------------+----------------
 326305       | AMIL ASSISTÊNCIA MÉDICA INTERNACIONAL S.A.               | 46186774089.06
 359017       | NOTRE DAME INTERMÉDICA SAÚDE S.A.                        | 21233847291.25
 368253       | HAPVIDA ASSISTENCIA MEDICA S.A.                          | 17517668817.45
 346659       | CAIXA DE ASSISTÊNCIA DOS FUNCIONÁRIOS DO BANCO DO BRASIL | 16669384973.04
 339679       | UNIMED NACIONAL - COOPERATIVA CENTRAL                    | 15693145145.11
 302147       | PREVENT SENIOR PRIVATE OPERADORA DE SAÚDE LTDA           | 13227001351.90
 343889       | UNIMED BELO HORIZONTE COOPERATIVA DE TRABALHO MÉDICO     | 11923246961.39
 323080       | GEAP AUTOGESTÃO EM SAÚDE                                 |  7836114478.37
 352501       | UNIMED PORTO ALEGRE - COOPERATIVA MÉDICA LTDA.           |  7390693645.19
 335690       | UNIMED CAMPINAS - COOPERATIVA DE TRABALHO MÉDICO         |  6909423093.51
*/


