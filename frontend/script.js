const form = document.getElementById('fitnessForm');
const output = document.getElementById('output');

form.addEventListener('submit', async function (e) {
    e.preventDefault();

    const data = new FormData(form);

    const requestData = {
        age: Number(data.get('age')),
        weight: Number(data.get('weight')),
        height: Number(data.get('height')),
        gender: data.get('gender'),
        activity_level: data.get('activity_level'),
        fitness_goal: data.get('fitness_goal'),
        dietary_restrictions: data.get('dietary_restrictions').split(',').map(s => s.trim()).filter(Boolean),
        injuries: data.get('injuries').split(',').map(s => s.trim()).filter(Boolean),
        preferred_workout_time: data.get('preferred_workout_time'),
        available_equipment: [data.get('available_equipment')],
        workout_days_per_week: Number(data.get('workout_days_per_week'))
    };

    try {
        const response = await fetch('http://localhost:8000/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(requestData)
        });

        if (!response.ok) throw new Error('Error getting response from AI');

        const result = await response.json();
        console.log(result);
        formatResponse(result);
    } catch (err) {
        output.textContent = 'Error: ' + err.message;
    }
});

function formatResponse(data) {
    const container = document.getElementById('formattedOutput');
    container.innerHTML = '';

    const workoutSection = document.createElement('div');
    workoutSection.className = 'section';
    workoutSection.innerHTML = `<h2>Workout Plan</h2>`;
    data.workout_plan.forEach(item => {
        workoutSection.innerHTML += `<p><strong>${item.name}</strong> (${item.muscle_group}): ${item.sets}x${item.reps} (rest: ${item.rest_time}s)</p>`;
    });

    const mealSection = document.createElement('div');
    mealSection.className = 'section';
    mealSection.innerHTML = `<h2>Meal Plan</h2>`;
    data.meal_plan.forEach(meal => {
        mealSection.innerHTML += `<p><strong>${meal.name}</strong> (${meal.timing})<br>Ingredients: ${meal.ingredients.join(', ')}<br>Portions: ${meal.portions.join(', ')}</p>`;
    });

    const macrosSection = document.createElement('div');
    macrosSection.className = 'section';
    macrosSection.innerHTML = `
        <h2>Daily Macronutrients</h2>
        <p>Calories: ${data.daily_calories}</p>
        <p>Protein: ${data.macros.protein}g</p>
        <p>Carbohydrates: ${data.macros.carbs}g</p>
        <p>Fats: ${data.macros.fats}g</p>
    `;

    const weekSection = document.createElement('div');
    weekSection.className = 'section';
    weekSection.innerHTML = `<h2>Weekly Schedule</h2>`;

    const daysOrder = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];
    daysOrder.forEach(day => {
        const workout = data.weekly_schedule[day];
        if (workout) {
            weekSection.innerHTML += `
            <p><strong>${capitalize(day)}:</strong> ${workout}</p>
        `;
        }
    });

    const tipsSection = document.createElement('div');
    tipsSection.className = 'section';
    tipsSection.innerHTML = `<h2>Tips</h2><ul>`;
    data.tips.forEach(tip => {
        tipsSection.innerHTML += `<li>${tip}</li>`;
    });
    tipsSection.innerHTML += `</ul>`;

    const quoteSection = document.createElement('div');
    quoteSection.className = 'section';
    quoteSection.innerHTML = `
        <h2>Motivational Quote</h2>
        <blockquote>${data.motivational_quote}</blockquote>
    `;

    container.append(
        workoutSection,
        mealSection,
        macrosSection,
        weekSection,
        tipsSection,
        quoteSection
    );
}

function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}
