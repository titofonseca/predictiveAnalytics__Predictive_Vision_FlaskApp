const metricSelect = document.getElementById("metric-select");
const predictBtn = document.getElementById("predict-btn");
const forecastChartCanvas = document.getElementById("forecast-chart");
let forecastChart;

const metrics = ["Revenue", "Sessions", "Conversions"];
metrics.forEach(metric => {
    const option = document.createElement("option");
    option.value = metric;
    option.textContent = metric;
    metricSelect.appendChild(option);
});

function createChart(dates, realValues, predictedValues, upperBound, lowerBound) {
    if (forecastChart) {
        forecastChart.destroy();
    }

    const gradientFill = forecastChartCanvas.getContext('2d').createLinearGradient(0, 0, 0, 400);
    gradientFill.addColorStop(0, 'rgba(135, 206, 235, 0.5)');
    gradientFill.addColorStop(1, 'rgba(135, 206, 235, 0.5)');

    forecastChart = new Chart(forecastChartCanvas, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [
                {
                    label: 'Real Values',
                    data: realValues,
                    borderColor: 'rgba(0, 0, 139, 1)', // Azul escuro
                    backgroundColor: 'transparent',
                    fill: false,
                    borderWidth: 2,
                    pointRadius: 0,  // Remove os pontos
                },
                {
                    label: 'Predicted Values',
                    data: predictedValues,
                    borderColor: 'rgba(255, 0, 0, 1)', // Vermelho
                    backgroundColor: 'transparent',
                    fill: false,
                    borderWidth: 2,
                    pointRadius: 0,  // Remove os pontos
                    borderDash: [5, 5],
                },
                {
                    label: 'Confidence Interval',
                    data: upperBound,
                    borderColor: gradientFill,
                    backgroundColor: gradientFill,
                    fill: '-1',
                    pointRadius: 0,  // Remove os pontos
                },
                {
                    label: '',
                    data: lowerBound,
                    borderColor: gradientFill,
                    backgroundColor: gradientFill,
                    fill: '1',
                    pointRadius: 0,  // Remove os pontos
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Forecasting Analytics'
                },
                zoom: {
                    zoom: {
                        wheel: {
                            enabled: true,
                        },
                        pinch: {
                            enabled: true
                        },
                        mode: 'xy'
                    },
                    pan: {
                        enabled: true,
                        mode: 'xy',
                        speed: 20,
                        threshold: 10
                    }
                }
            },
            interaction: {
                mode: 'index',
                intersect: false
            },
            scales: {
                x: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Date'
                    }
                },
                y: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Value'
                    }
                }
            }
        }
    });
}

// Evento de clique para o botão "Prever"
predictBtn.addEventListener("click", function(e) {
    e.preventDefault();

    const selectedMetric = metricSelect.value;

    // Mostrar o overlay de carregamento e ocultar o gráfico
    const loadingOverlay = document.getElementById("loading-overlay");
    loadingOverlay.classList.remove("d-none");
    loadingOverlay.classList.add("d-flex");
    forecastChartCanvas.style.display = 'none';

    // Solicitação AJAX para buscar os dados
    fetch(`/get_data?metric=${selectedMetric}`)
        .then(response => response.json())
        .then(data => {
            // Atualizar a visualização com os dados recebidos
            createChart(data.dates, data.real_values, data.predicted_values, data.upper_bound, data.lower_bound);

            // Esconder o overlay de carregamento e mostrar o gráfico
            loadingOverlay.classList.remove("d-flex");
            loadingOverlay.classList.add("d-none");
            forecastChartCanvas.style.display = 'block';
        })
        .catch(error => {
            console.error("Erro ao buscar os dados:", error);
            
            // Esconder o overlay de carregamento em caso de erro
            loadingOverlay.classList.remove("d-flex");
            loadingOverlay.classList.add("d-none");
            forecastChartCanvas.style.display = 'block';

            if(forecastChart) {
                forecastChart.resize(); // Garante que o gráfico seja renderizado corretamente
            }
        });
});

// Evento de clique para o botão "Exportar como CSV"
const exportCsvBtn = document.getElementById("export-csv-btn");
exportCsvBtn.addEventListener("click", function() {
    const selectedMetric = metricSelect.value;

    // Mudar o texto e ícone do botão para o ícone de carregamento
    exportCsvBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Exporting...';

    // Assumindo que a exportação demora 2 segundos
    setTimeout(function() {
        // Mudar o ícone para o "visto" após a exportação
        exportCsvBtn.innerHTML = '<i class="fas fa-check"></i> Exported!';

        // Reverter para o texto e ícone originais após 2 segundos de confirmação
        setTimeout(function() {
            exportCsvBtn.innerHTML = '<i class="fas fa-file-csv"></i> Export as CSV';
        }, 2000);

    }, 2000);

    window.location.href = `/export_csv?metric=${selectedMetric}`;
});