
function category_chart(data)
{

    Highcharts.chart('category_chart', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Issues per Category'
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            type: 'Category',
            labels: {
                rotation: -45,
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                },
                formatter: function() { return data[this.value]['issue_category'];},
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Staff'
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            pointFormat: 'Issue: <b>{point.y:.1f}</b>'
        },
        series: [{
            name: 'category',
            data: data,
            dataLabels: {
                enabled: true,
//                rotation: -90,
                color: '#FFFFFF',
                align: 'right',
                format: '{point.y}', // one decimal
//                y: 10, // 10 pixels down from the top
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        }]
    });
}

function organization_chart(data)
{

    Highcharts.chart('organization_chart', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Issues per Organization'
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            type: 'Category',
            labels: {
                rotation: -45,
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                },
                formatter: function() { return data[this.value]['reported_by__last_name'];},
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Staff'
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            pointFormat: 'Issue: <b>{point.y:.1f}</b>'
        },
        series: [{
            name: 'category',
            data: data,
            dataLabels: {
                enabled: true,
//                rotation: -90,
                color: '#FFFFFF',
                align: 'right',
                format: '{point.y}', // one decimal
//                y: 10, // 10 pixels down from the top
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        }]
    });
}

function month_chart(data)
{

    Highcharts.chart('month_chart', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Issues per Month'
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            type: 'Category',
            labels: {
                rotation: -45,
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                },
                formatter: function() { return data[this.value]['month'];},
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Staff'
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            pointFormat: 'Issue: <b>{point.y:.1f}</b>'
        },
        series: [{
            name: 'category',
            data: data,
            dataLabels: {
                enabled: true,
//                rotation: -90,
                color: '#FFFFFF',
                align: 'right',
                format: '{point.y}', // one decimal
//                y: 10, // 10 pixels down from the top
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        }]
    });
}


function target_chart(data)
{
    Highcharts.chart('target_chart', {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
//            type: 'variablepie'
        },
        title: {
            text: 'Issues per Target Population'
        },
        subtitle: {
            text: ''
        },
        accessibility: {
            point: {
            valueSuffix: '%'
            }
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: false
                },
                showInLegend: true
            }
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        series: [{
            name: 'Target Population',
//            colorByPoint: true,
//            minPointSize: 10,
//            innerSize: '20%',
//            zMin: 0,
            data: data,
            dataLabels: {
                enabled: true,
//                rotation: -90,
                color: '#FFFFFF',
                align: 'right',
                format: '{point.y} - <b>{point.percentage:.1f}%</b>',
//                format: '{point.y:.1f}', // one decimal
//                y: 10, // 10 pixels down from the top
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        }],
    });
}

function source_chart(typeData)
{
    Highcharts.chart('source_chart', {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'Issues per Source'
        },
        subtitle: {
            text: ''
        },
        accessibility: {
            point: {
            valueSuffix: '%'
            }
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: false
                },
                showInLegend: true
            }
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        series: [{
            name: 'Source',
            colorByPoint: true,
            data: typeData,
            dataLabels: {
                enabled: true,
//                rotation: -90,
                color: '#FFFFFF',
                align: 'right',
                format: '{point.y} - <b>{point.percentage:.1f}%</b>', // one decimal
//                y: 10, // 10 pixels down from the top
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        }],
    });
}

function InitialiseTypeChart1(typeData)
{
Highcharts.chart('type_count', {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: 0,
        plotShadow: false
    },
    title: {
        text: 'Staff<br>type',
        align: 'center',
        verticalAlign: 'middle',
        y: 60
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            dataLabels: {
                enabled: true,
                distance: -50,
                style: {
                    fontWeight: 'bold',
                    color: 'white'
                }
            },
            startAngle: -90,
            endAngle: 90,
            center: ['50%', '75%'],
            size: '110%'
        }
    },
    series: [{
        type: 'pie',
        name: 'Type',
        innerSize: '50%',
        data: typeData,
    }]
});

}

function InitialiseDutyStationChart(dutyStationData)
{
    Highcharts.chart('duty_station_count', {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'Distribution By Duty Station'
        },
        subtitle: {
            text: ''
        },
        accessibility: {
            point: {
            valueSuffix: '%'
            }
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: false
                },
                showInLegend: true
            }
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        series: [{
            name: 'Duty station',
            colorByPoint: true,
            data: dutyStationData,
            dataLabels: {
                enabled: true,
//                rotation: -90,
                color: '#FFFFFF',
                align: 'right',
                format: '{point.y}', // one decimal
//                y: 10, // 10 pixels down from the top
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        }],
    });
}

function InitialiseBsafeChart(number_of_employees,employees_conpleted_bsafe_count)
{
    Highcharts.chart('bSafe_gauge', {

    chart: {
        type: 'gauge',
        plotBackgroundColor: null,
        plotBackgroundImage: null,
        plotBorderWidth: 0,
        plotShadow: false
    },

    title: {
        text: 'Staff Completed Bsafe training'
    },

    pane: {
        startAngle: -150,
        endAngle: 150,
        background: [{
            backgroundColor: {
                linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                stops: [
                    [0, '#FFF'],
                    [1, '#333']
                ]
            },
            borderWidth: 0,
            outerRadius: '109%'
        }, {
            backgroundColor: {
                linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                stops: [
                    [0, '#333'],
                    [1, '#FFF']
                ]
            },
            borderWidth: 1,
            outerRadius: '107%'
        }, {
            // default background
        }, {
            backgroundColor: '#DDD',
            borderWidth: 0,
            outerRadius: '105%',
            innerRadius: '103%'
        }]
    },

    // the value axis
    yAxis: {
        min: 0,
        max: number_of_employees,

        minorTickInterval: 'auto',
        minorTickWidth: 1,
        minorTickLength: 10,
        minorTickPosition: 'inside',
        minorTickColor: '#666',

        tickPixelInterval: 30,
        tickWidth: 2,
        tickPosition: 'inside',
        tickLength: 10,
        tickColor: '#666',
        labels: {
            step: 2,
            rotation: 'auto'
        },
        title: {
            text: 'km/h'
        },
        plotBands: [{
            from: 0,
            to: 120,
            color: '#DF5353' // red
        }, {
            from: 120,
            to: 160,
            color: '#DDDF0D' // yellow
        }, {
            from: 160,
            to: number_of_Staff,
            color: '#55BF3B' // greed
        }]
    },

    series: [{
        name: 'Speed',
        data: [employees_conpleted_bsafe_count],
        tooltip: {
            valueSuffix: ' km/h'
        }
    }]

},
// Add some life
function (chart) {
    if (!chart.renderer.forExport) {
        setInterval(function () {
            var point = chart.series[0].points[0],
                newVal,
                inc = Math.round((Math.random() - 0.5) * 20);

            newVal = point.y + inc;
            if (newVal < 0 || newVal > number_of_employees) {
                newVal = point.y - inc;
            }

            point.update(newVal);

        }, 3000);
    }
});
}

// Security Dashboard
function InitialiseSecurityDashboard(departmentData, dependentTypeData, dependentOfficeInCountryCount, dependentOfficeOutsideCountryCount)
{
    $( document ).ready(function() {
        //InitialiseDepartmentChart(departmentData);
        InitialiseDependentTypeChart(dependentTypeData);
//        InitialiseEmoloyeeDependentChart();
        InitialiseDependentOfficeInCountryChart(dependentOfficeInCountryCount)
        InitialiseDependentOfficeOutsideCountryChart(dependentOfficeOutsideCountryCount)
    });
}
function InitialiseDepartmentChart(departmentData)
{

    Highcharts.chart('employee_department', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Distribution By Section'
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            type: 'Section',
            labels: {
                rotation: -45,
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                },
                formatter: function() { return departmentData[this.value]['name'];},
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Total Staff'
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            pointFormat: 'Total Staff: <b>{point.y:.1f}</b>'
        },
        series: [{
            name: 'Section Staff',
            data: departmentData,
            dataLabels: {
                enabled: true,
//                rotation: -90,
                color: '#FFFFFF',
                align: 'right',
                format: '{point.y}', // one decimal
//                y: 10, // 10 pixels down from the top
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        }]
    });
}

function InitialiseDependentOfficeInCountryChart(dependentOfficeInCountryCount)
{

    Highcharts.chart('dependent_count_person_office_in_country', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Dependents Inside Country By Duty Station'
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            type: 'Office',
            labels: {
                rotation: -45,
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                },
                formatter: function() { return dependentOfficeInCountryCount[this.value]['name'];},
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Total of Staff'
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            pointFormat: 'Total Staff: <b>{point.y:.1f}</b>'
        },
        series: [{
            name: 'Office Dependents',
            data: dependentOfficeInCountryCount,
            dataLabels: {
                enabled: true,
//                rotation: -90,
                color: '#FFFFFF',
                align: 'right',
                format: '{point.y}', // one decimal
//                y: 10, // 10 pixels down from the top
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        }]
    });
}

function InitialiseDependentOfficeOutsideCountryChart(dependentOfficeOutsideCountryCount)
{

    Highcharts.chart('dependent_count_person_office_outside_country', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Dependents Outside Country By Duty Station'
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            type: 'Office',
            labels: {
                rotation: -45,
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                },
                formatter: function() { return dependentOfficeOutsideCountryCount[this.value]['name'];},
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Total Staff'
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            pointFormat: 'Total Staff: <b>{point.y:.1f}</b>'
        },
        series: [{
            name: 'Office Dependents',
            data: dependentOfficeOutsideCountryCount,
            dataLabels: {
                enabled: true,
//                rotation: -90,
                color: '#FFFFFF',
                align: 'right',
                format: '{point.y}', // one decimal
//                y: 10, // 10 pixels down from the top
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        }]
    });
}

function InitialiseDependentTypeChart(dependentTypeData)
{
    Highcharts.chart('dependent_count_person_type', {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'Dependents Distribution: National/International'
        },
        subtitle: {
            text: ''
        },
        accessibility: {
            point: {
            valueSuffix: '%'
            }
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: false
                },
                showInLegend: true
            }
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        series: [{
            name: 'Type',
            colorByPoint: true,
            data: dependentTypeData,
            dataLabels: {
                enabled: true,
//                rotation: -90,
                color: '#FFFFFF',
                align: 'right',
                format: '{point.y}', // one decimal
//                y: 10, // 10 pixels down from the top
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }
        }],
    });
}


function InitialiseEmployeeDependentChart()
{

    Highcharts.chart('person_dependent_office', {
        data: {
            table: 'personDependentDataTable'
        },
        chart: {
            type: 'column'
        },
        title: {
            text: 'Personnel and Dependent by Office and Contract Type'
        },
        yAxis: {
            allowDecimals: false,
            title: {
                text: 'Office Personnel'
            }
        },
        tooltip: {
            formatter: function () {

                return '<b>' + this.series.name + '</b><br/>' +
                    this.point.y + ' ' + this.point.name.toLowerCase();

            }
        }
    });


}


